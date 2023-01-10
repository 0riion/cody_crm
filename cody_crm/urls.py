from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

API_VERSION = 'v1'

urlpatterns = [
    path(f'{API_VERSION}/admin/', admin.site.urls),
    path(f'{API_VERSION}/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_VERSION}/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{API_VERSION}/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(f'{API_VERSION}/api/', include('services.users.urls')),
    path(f'{API_VERSION}/api/', include('services.states.urls')),
]
