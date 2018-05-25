from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from marketplace.supporters.api.v1.serializers import SupporterRegistrationSerializer
from marketplace.supporters.models import Supporter
from marketplace.users.models import User


class SupporterRegistrationView(APIView):

    def post(self, request):
        serializer = SupporterRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create_user(email=serializer.validated_data['email'],
                                            password=serializer.validated_data['password'])

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            supporter = Supporter.objects.create(user=user)

        return Response(data={'token': token}, status=status.HTTP_201_CREATED)
