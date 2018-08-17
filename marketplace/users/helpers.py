from rest_framework_jwt.settings import api_settings


def is_supporter(user):
    return hasattr(user, 'supporter')


def is_athlete(user):
    return hasattr(user, 'athlete')


def jwt_payload(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)
