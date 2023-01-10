from rest_framework.routers import DefaultRouter
from .views import OrderStatusView

router = DefaultRouter()
router.register(r'order-status', OrderStatusView, basename='order-status')
urlpatterns = router.urls

