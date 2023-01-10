from rest_framework.routers import DefaultRouter
from .views import StateView

router = DefaultRouter()
router.register(r'states', StateView, basename='states')
urlpatterns = router.urls
