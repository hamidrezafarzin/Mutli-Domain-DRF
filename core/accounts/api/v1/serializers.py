from rest_framework import serializers
from accounts.models import User, Profile
import tempfile
from django.core.exceptions import ValidationError
from utils.errors.constants import Errors

class RegisterSerializer(serializers.ModelSerializer):
    """Registration serializer with password checkup"""

    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["phone", "password", "password1"]

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(Errors.PASSWORD_MISMATCH)
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to manage extra user info"""

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
        ]