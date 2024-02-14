from netpoint.api.routers import NetPointRouter
from . import views


router = NetPointRouter()
router.APIRootView = views.VirtualizationRootView

# Clusters
router.register('cluster-types', views.ClusterTypeViewSet)
router.register('cluster-groups', views.ClusterGroupViewSet)
router.register('clusters', views.ClusterViewSet)

# VirtualMachines
router.register('virtual-machines', views.VirtualMachineViewSet)
router.register('interfaces', views.VMInterfaceViewSet)
router.register('virtual-disks', views.VirtualDiskViewSet)

app_name = 'virtualization-api'
urlpatterns = router.urls
