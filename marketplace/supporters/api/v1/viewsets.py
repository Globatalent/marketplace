from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from marketplace.supporters.models import Alert
from marketplace.supporters.api.v1.serializers import AlertSerializer


class AlertViewSet(CreateModelMixin,
                   ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()

    def create(self, request, *args, **kwargs):
        if not (hasattr(request.user, 'supporter')):
            raise PermissionDenied

        self.request.data['supporter'] = request.user.supporter.id

        return super().create(request=request)


