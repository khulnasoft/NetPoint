from netpoint.api.routers import NetPointRouter
from . import views


router = NetPointRouter()
router.APIRootView = views.WirelessRootView

router.register('wireless-lan-groups', views.WirelessLANGroupViewSet)
router.register('wireless-lans', views.WirelessLANViewSet)
router.register('wireless-links', views.WirelessLinkViewSet)

app_name = 'wireless-api'
urlpatterns = router.urls
