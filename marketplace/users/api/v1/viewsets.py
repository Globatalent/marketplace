from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from marketplace.users.api.v1.serializers import UserSerializer
from marketplace.users.models import User


class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = UserSerializer(instance=request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
