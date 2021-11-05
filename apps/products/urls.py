from rest_framework.routers import DefaultRouter

from apps.products.views import MenuViewSet

app_name = "products"

router = DefaultRouter()
router.register(r"menus", MenuViewSet)

urlpatterns = router.urls
