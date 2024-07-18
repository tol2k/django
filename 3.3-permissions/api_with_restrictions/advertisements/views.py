
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvFilter


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    def perform_update(self, serializer):
        serializer.save(creator=self.request.user)
    def perform_destroy(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()]
        return []



