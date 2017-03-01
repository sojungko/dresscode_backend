from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', views.UserList.as_view()),
    # url(r'^api/users/', include('user.api.urls'), namespace='users-api')
]

urlpatterns = format_suffix_patterns(urlpatterns)
