from rest_framework.viewsets import ReadOnlyModelViewSet
from marketplace.supporters.models import Alert
from marketplace.supporters.api.v1.serializers import AlertSerializer


class AlertViewSet(ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


