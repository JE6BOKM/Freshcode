from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.serializers import ChooseSerializerClassMixin
from apps.products.models import Menu
from apps.products.serializers import CreateUpdateMenuSerialier, MenuSerialier
from apps.users.permissions import IsAdmin


class MenuViewSet(ChooseSerializerClassMixin, ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialier
    serializer_classes = {
        "create": CreateUpdateMenuSerialier,
        "update": CreateUpdateMenuSerialier,
        "partial_update": CreateUpdateMenuSerialier,
    }

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["create", "update", "partial_update", "delete"]:
            self.permission_classes = [IsAdmin]

        return super().get_permissions()
