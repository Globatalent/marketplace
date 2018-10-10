from marketplace.actions.constants import FOLLOWS, UNFOLLOWS, ADD_PICTURE, PURCHASE


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


def _extract_actor_trigger_target_save_purchase(*args, **kwargs):
    """Extracts actor, trigger and target from the args and kwargs given as parameters,
    assuming there was a save method call for a model.
    """
    from marketplace.purchases.models import Purchase

    assert len(args) >= 1, 'There should be at last a self argument'
    assert isinstance(args[0], Purchase), 'The instance should be a Picture'
    assert args[0].pk is not None, 'The model should be saved'

    actor = args[0].user
    trigger = args[0]
    target = args[0].token.campaign
    return actor, trigger, target


def extract_actor_trigger_target(verb, method, *args, **kwargs):
    """Selects the correct function to extract the actor, trigger and target from the action."""
    handlers = {
        FOLLOWS: _extract_actor_trigger_target_method,
        UNFOLLOWS: _extract_actor_trigger_target_method,
        PURCHASE: _extract_actor_trigger_target_save_purchase,
    }
    default_handler = _extract_actor_trigger_target_method if method else _extract_actor_trigger_target
    return handlers.get(verb, default_handler)(*args, **kwargs)


def _human_readable_default(action):
    """Makes an action human readable."""
    text = "{} {}".format(str(action.actor), action.verb)
    if action.trigger:
        text = "{} {}".format(text, str(action.trigger))
    if action.target:
        text = "{} {}".format(text, str(action.target))
    return text


def _human_readable_purchase(action):
    """Makes an action human readable."""
    text = "{} has invested {} in {}".format(str(action.actor), str(action.trigger), str(action.target))
    return text


def _human_readable_picture(action):
    """Makes an action human readable."""
    text = "{} {}".format(str(action.actor), action.verb)
    return text


def human_readable(action):
    """Makes an action human readable."""
    handlers = {
        ADD_PICTURE: _human_readable_picture,
        PURCHASE: _human_readable_purchase,
    }  # Use to specify special handlers to verbs
    default_handler = _human_readable_default
    return handlers.get(action.verb, default_handler)(action)
