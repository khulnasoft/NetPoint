from netpoint.api.routers import NetPointRouter
from . import views


router = NetPointRouter()
router.APIRootView = views.CoreRootView

# Data sources
router.register('data-sources', views.DataSourceViewSet)
router.register('data-files', views.DataFileViewSet)

# Jobs
router.register('jobs', views.JobViewSet)

app_name = 'core-api'
urlpatterns = router.urls
