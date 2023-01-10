from rest_framework.routers import DefaultRouter
from .views import CustomerView

router = DefaultRouter()
router.register(r'customers', CustomerView, basename='customers')
urlpatterns = router.urls
