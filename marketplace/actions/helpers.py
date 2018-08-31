from marketplace.actions.constants import FOLLOWS, UNFOLLOWS, ADD_PICTURE, ADD_REVIEW


def _extract_actor_trigger_target_method(*args, **kwargs):
    """Extracts actor, trigger and target from the args and kwargs given as parameters,
    assuming there was a method call.
    """
    assert len(args) >= 2, "For a method, an argument extra, actor, is mandatory"
    actor = args[0]
    trigger = args[1]
    target = args[2] if len(args) > 2 else None
    return actor, trigger, target


def _extract_actor_trigger_target(*args, **kwargs):
    """Extracts actor, trigger and target from the args and kwargs given as parameters,
    assuming there was a function call.
    """
    assert len(args) >= 1, "For a function you must specify an actor."
    actor = args[0]
    trigger = args[1] if len(args) > 1 else None
    target = args[2] if len(args) > 2 else None
    return actor, trigger, target


def _extract_actor_trigger_target_add_picture(*args, **kwargs):
    """Extracts actor, trigger and target from the args and kwargs given as parameters,
    assuming there was a save method call for a model.
    """
    from marketplace.athletes.models import Picture

    assert len(args) >= 1, 'There should be at last a self argument'
    assert isinstance(args[0], Picture), 'The instance should be a Picture'
    assert args[0].pk is not None, 'The model should be saved'

    actor = args[0].athlete
    trigger = args[0]
    target = None
    return actor, trigger, target


def _extract_actor_trigger_target_add_review(*args, **kwargs):
    """Extracts actor, trigger and target from the args and kwargs given as parameters,
    assuming there was a save method call for a model.
    """
    from marketplace.athletes.models import Review

    assert len(args) >= 1, 'There should be at last a self argument'
    assert isinstance(args[0], Review), 'The instance should be a Picture'
    assert args[0].pk is not None, 'The model should be saved'

    actor = args[0].reviewer
    trigger = args[0]
    target = args[0].athlete
    return actor, trigger, target


def extract_actor_trigger_target(verb, method, *args, **kwargs):
    handlers = {
        FOLLOWS: _extract_actor_trigger_target_method,
        UNFOLLOWS: _extract_actor_trigger_target_method,
        ADD_PICTURE: _extract_actor_trigger_target_add_picture,
        ADD_REVIEW: _extract_actor_trigger_target_add_review,
    }
    default_handler = _extract_actor_trigger_target_method if method else _extract_actor_trigger_target
    return handlers.get(verb, default_handler)(*args, **kwargs)
