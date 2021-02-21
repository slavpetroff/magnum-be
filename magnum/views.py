from rest_framework.viewsets import ModelViewSet

from magnum.models import User
from magnum.serializers import UserSerializer


class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
