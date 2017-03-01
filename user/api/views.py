from rest_framework.generics import ListAPIView
from user.models import User

class UserListAPIView(ListAPIView):
    queryset = User.object.all()
