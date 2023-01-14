from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from services.users import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls