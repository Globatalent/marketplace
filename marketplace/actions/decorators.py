from django.contrib.contenttypes.models import ContentType


def dispatch_action(verb, method=False):
    """Decorator to dispatch and action when a method or function is called.

    Example:

    @trigger_action("verb", method=True)
    def method(self, trigger, target=None):
        # self is the actor
        pass

    @trigger_action("verb text")
    def func(actor, trigger=None, target=None):
        pass
    """

    def _decorator(func):
        """Decorator itself."""

        def _wrapper_trigger_action(*args, **kwargs):
            from marketplace.actions.models import Action

            """Wrapped function with the decorator."""
            result = func(*args, **kwargs)
            if method:
                assert len(args) >= 2, "For a method, an argument extra, actor, is mandatory"
                actor = args[0]
                trigger = args[1]
                target = args[2] if len(args) > 2 else None
            else:
                assert len(args) >= 1, "For a function you must specify an actor."
                actor = args[0]
                trigger = args[1] if len(args) > 1 else None
                target = args[2] if len(args) > 2 else None
            action = Action(
                actor_content_type=ContentType.objects.get_for_model(actor),
                actor_object_id=actor.pk,
                verb=verb,
            )
            if trigger and hasattr(trigger, "id"):
                action.trigger_content_type = ContentType.objects.get_for_model(trigger)
                action.trigger_object_id = trigger.pk
            if target and hasattr(target, "id"):
                action.target_content_type = ContentType.objects.get_for_model(target)
                action.target_object_id = target.pk
            action.save()
            return result

        return _wrapper_trigger_action

    return _decorator
