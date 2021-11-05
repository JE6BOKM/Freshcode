from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


from apps.products.models import Menu
from apps.products.serializers import MenuSeiralier
from apps.users.permissions import IsAdmin


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSeiralier

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [permissions.AllowAny]
        elif self.action == "craete":
            self.permission_classes = [IsAdmin]
        return super().get_permissions()
