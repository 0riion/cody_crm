from rest_framework.routers import DefaultRouter
from .views import WarehouseView

router = DefaultRouter()
router.register(r'warehouses', WarehouseView, basename='warehouses')
urlpatterns = router.urls
