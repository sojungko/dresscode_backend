from rest_framework.generics import ListAPIView
from user.models import User
from user.api.serializers import UserSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
