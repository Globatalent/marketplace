from rest_framework_jwt.settings import api_settings


def jwt_payload(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


def restore_password(restore_password_code, password):
    """Restore the password of the user with the restore_password_code code."""
    from marketplace.users.models import User

    user = User.objects.get(restore_password_code=restore_password_code)
    user.set_password(password)
    user.save()


def verify_email(verification_code):
    from marketplace.users.models import User

    user = User.objects.get(verification_code=verification_code)
    user.verify()
    user.save()


def is_following(user, campaign):
    """Checks if the given user is following the given campaign."""
    if user.is_authenticated:
        return user.following.filter(pk=campaign.pk).exists()
    return False
