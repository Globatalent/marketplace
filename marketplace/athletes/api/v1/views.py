from django.db import transaction
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace.athletes.api.v1.serializers import AthleteRegistrationSerializer
from marketplace.athletes.models import Athlete
from marketplace.users.models import User
from marketplace.users.helpers import jwt_payload


class AthleteRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AthleteRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create_user(email=serializer.validated_data['email'],
                                            password=serializer.validated_data['password'])
            token = jwt_payload(user)
            Athlete.objects.create(user=user, first_name=serializer.validated_data['first_name'],
                                   last_name=serializer.validated_data['last_name'],
                                   country=serializer.validated_data['country'],
                                   sex=serializer.validated_data['sex'],
                                   date_of_birth=serializer.validated_data['date_of_birth'],
                                   sport=serializer.validated_data['sport'])
        return Response(data={'token': token}, status=status.HTTP_201_CREATED)
