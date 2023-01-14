from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from services.users import views

router = DefaultRouter()

router.register('users', views.UserViewSet, basename="users")

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]

urlpatterns += router.urls