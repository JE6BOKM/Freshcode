from rest_framework.routers import DefaultRouter

from apps.products.views import CategoryCRUDViewSet, MenuCRUDViewSet, TagCRUDViewSet, ItemCRUDViewSet

app_name = "products"

router = DefaultRouter()
router.register(r"categories", CategoryCRUDViewSet)
router.register(r"menus", MenuCRUDViewSet)
router.register(r"tags", TagCRUDViewSet)
router.register(r"items", ItemCRUDViewSet)


urlpatterns = router.urls
