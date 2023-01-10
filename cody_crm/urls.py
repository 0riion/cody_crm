from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

API_VERSION = 'v1'
CHILD_API_PATH = 'api'

urlpatterns = [
    path(f'{API_VERSION}/admin/', admin.site.urls),
    path(f'{API_VERSION}/{CHILD_API_PATH}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_VERSION}/{CHILD_API_PATH}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{API_VERSION}/{CHILD_API_PATH}/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.users.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.states.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.city.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.address.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.category.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.order_status.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.provider.urls')),
    path(f'{API_VERSION}/{CHILD_API_PATH}/', include('services.customer.urls')),
]
