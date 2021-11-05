from rest_framework import serializers

from apps.core.serializers import DynamicFieldsSerializerMixin

from .models import User


class UserSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "role")
        read_only_fields = ("username",)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
        )
        extra_kwargs = {"password": {"write_only": True}}
