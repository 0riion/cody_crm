from rest_framework.routers import DefaultRouter
from .views import CategoryView

router = DefaultRouter()
router.register(r'categories', CategoryView, basename='categories')
urlpatterns = router.urls
