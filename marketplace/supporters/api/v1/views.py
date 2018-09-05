from django.db import transaction
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace.supporters.api.v1.serializers import SupporterRegistrationSerializer
from marketplace.supporters.models import Supporter
from marketplace.users.helpers import jwt_payload
from marketplace.users.models import User


class SupporterRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SupporterRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            token = jwt_payload(user)
            Supporter.objects.create(
                user=user,
                first_name=serializer.validated_data.get('first_name', ""),
                last_name=serializer.validated_data.get('last_name', "")
            )
        return Response(data={'token': token}, status=status.HTTP_201_CREATED)
