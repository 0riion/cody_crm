from django.urls import path
from services.authentication.views import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
]
