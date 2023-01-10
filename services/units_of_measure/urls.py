from rest_framework.routers import DefaultRouter
from .views import UnitOfMeasureView

router = DefaultRouter()
router.register(r'unit-of-measure', UnitOfMeasureView, basename='unit-of-measure')
urlpatterns = router.urls
