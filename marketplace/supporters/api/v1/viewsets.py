from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from marketplace.supporters.models import Alert
from marketplace.supporters.api.v1.serializers import AlertSerializer


class AlertViewSet(CreateModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()

    def create(self, request, *args, **kwargs):
        if not (hasattr(request.user, 'supporter')):
            raise PermissionDenied

        self.request.data['supporter'] = request.user.supporter.id

        return super().create(request=request)

    def get_queryset(self):
        return Alert.objects.filter(supporter__exact=self.request.user.supporter.id)

    def update(self, request, *args, **kwargs):
        if not (hasattr(request.user, 'supporter')):
            raise PermissionDenied

        kwargs['partial'] = True
        return super().update(request=request, *args, **kwargs)

