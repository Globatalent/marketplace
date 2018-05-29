from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _
from marketplace.athletes.models import Picture, Link, Athlete
from marketplace.users.models import User


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image',)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('name', 'url', 'athlete')


class AthleteSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'country', 'sex', 'date_of_birthday',
                  'sport', 'state', 'pictures', 'links')


class AthleteRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField()
    sex = serializers.CharField()
    date_of_birthday = serializers.DateField()
    sport = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message=_('There is another user with this email'))])
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    repeat_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_password(self, data):
        password_validation.validate_password(password=data, user=User)
        return data

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Password does not match the confirm password.")
        return data

