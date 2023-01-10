from rest_framework.routers import DefaultRouter
from .views import ProductView

router = DefaultRouter()
router.register(r'product', ProductView, basename='product')
urlpatterns = router.urls
