from rest_framework.routers import DefaultRouter
from .views import CityView

router = DefaultRouter()
router.register(r'cities', CityView, basename='cities')
urlpatterns = router.urls

