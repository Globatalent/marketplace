from django.views.generic import DetailView
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet, GenericViewSet
from marketplace.supporters.models import Alert
from marketplace.supporters.api.v1.serializers import AlertSerializer


class AlertViewSet(CreateModelMixin,
                   UpdateModelMixin,
                   ReadOnlyModelViewSet,
                   DetailView):
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
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        instance.rule = serializer.validated_data['rule']
        instance.amount = serializer.validated_data['amount']

        return super().update(request=request)
