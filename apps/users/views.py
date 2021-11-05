from rest_framework import viewsets

from .models import User
from .permissions import IsAdmin
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["list"]:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()
