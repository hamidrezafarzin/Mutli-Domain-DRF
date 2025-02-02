from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import (
    DomainSerializer
)
from multidomains.models import Domain
from rest_framework import viewsets
from rest_framework.decorators import action
from utils.domain_handler.cloudflare_client import CloudflareAPIClient
from django.conf import settings
class DomainViewSet(viewsets.ModelViewSet):
    serializer_class = DomainSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Domain.objects.filter(user=self.request.user)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], name="activation")
    def activation(self, request, pk=None):
        object = self.get_object()
        if not object.is_active:
            Cloudflare_api = CloudflareAPIClient()
            zone_detail = Cloudflare_api.get_zone_details(zone_id=object.zone)
            if Cloudflare_api.is_zone_active(zone_detail):
                object.active()
                return Response({"detail": "Zone active."}, status=status.HTTP_200_OK)
            else:   
                return Response({"detail": "Zone is not active."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"detail": "Domain already active."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], name="set_dns")
    def set_dns(self, request, pk=None):
        object = self.get_object()
        if object.is_active:
            Cloudflare_api = CloudflareAPIClient()
            zone_detail = Cloudflare_api.add_dns_a_record(zone_id=object.zone, name="@", ip=settings.DESTINATION_IP, proxied=True)
            return Response({"detail": "Dns Set successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "Zone is not active."}, status=status.HTTP_406_NOT_ACCEPTABLE)