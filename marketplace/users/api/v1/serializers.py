from rest_framework import serializers

from marketplace.athletes.api.v1.serializers import AthleteSerializer
from marketplace.supporters.api.v1.serializers import SupporterSerializer
from marketplace.users.models import User


class UserSerializer(serializers.ModelSerializer):
    athlete = AthleteSerializer(read_only=True)
    supporter = SupporterSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'athlete', 'supporter', 'is_staff')
