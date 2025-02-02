from rest_framework import serializers
from django.core.exceptions import ValidationError
from multidomains.models import Domain
from utils.errors.constants import Errors
from utils.domain_handler.cloudflare_client import CloudflareAPIClient

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name', "zone", "name_servers", "is_created", 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', "zone", "name_servers", "is_created", 'is_active', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        
        cloudflare_api = CloudflareAPIClient()
        domain_created = cloudflare_api.create_zone(validated_data["name"])
        validated_data["zone"] = domain_created.id
        validated_data["name_servers"] = domain_created.name_servers
        validated_data["is_created"] = True
        return super().create(validated_data)
    