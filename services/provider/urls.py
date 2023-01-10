from rest_framework.routers import DefaultRouter
from .views import ProviderView

router = DefaultRouter()
router.register(r'providers', ProviderView, basename='providers')
urlpatterns = router.urls
