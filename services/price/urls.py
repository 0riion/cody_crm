from rest_framework.routers import DefaultRouter
from .views import PriceView

router = DefaultRouter()
router.register(r'price', PriceView, basename='price')
urlpatterns = router.urls
