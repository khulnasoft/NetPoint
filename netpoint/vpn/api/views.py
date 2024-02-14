from rest_framework.routers import APIRootView

from netpoint.api.viewsets import NetPointModelViewSet
from utilities.utils import count_related
from vpn import filtersets
from vpn.models import *
from . import serializers

__all__ = (
    'IKEPolicyViewSet',
    'IKEProposalViewSet',
    'IPSecPolicyViewSet',
    'IPSecProfileViewSet',
    'IPSecProposalViewSet',
    'L2VPNViewSet',
    'L2VPNTerminationViewSet',
    'TunnelGroupViewSet',
    'TunnelTerminationViewSet',
    'TunnelViewSet',
    'VPNRootView',
)


class VPNRootView(APIRootView):
    """
    VPN API root view
    """
    def get_view_name(self):
        return 'VPN'


#
# Viewsets
#

class TunnelGroupViewSet(NetPointModelViewSet):
    queryset = TunnelGroup.objects.annotate(
        tunnel_count=count_related(Tunnel, 'group')
    )
    serializer_class = serializers.TunnelGroupSerializer
    filterset_class = filtersets.TunnelGroupFilterSet


class TunnelViewSet(NetPointModelViewSet):
    queryset = Tunnel.objects.prefetch_related('ipsec_profile', 'tenant').annotate(
        terminations_count=count_related(TunnelTermination, 'tunnel')
    )
    serializer_class = serializers.TunnelSerializer
    filterset_class = filtersets.TunnelFilterSet


class TunnelTerminationViewSet(NetPointModelViewSet):
    queryset = TunnelTermination.objects.prefetch_related('tunnel')
    serializer_class = serializers.TunnelTerminationSerializer
    filterset_class = filtersets.TunnelTerminationFilterSet


class IKEProposalViewSet(NetPointModelViewSet):
    queryset = IKEProposal.objects.all()
    serializer_class = serializers.IKEProposalSerializer
    filterset_class = filtersets.IKEProposalFilterSet


class IKEPolicyViewSet(NetPointModelViewSet):
    queryset = IKEPolicy.objects.all()
    serializer_class = serializers.IKEPolicySerializer
    filterset_class = filtersets.IKEPolicyFilterSet


class IPSecProposalViewSet(NetPointModelViewSet):
    queryset = IPSecProposal.objects.all()
    serializer_class = serializers.IPSecProposalSerializer
    filterset_class = filtersets.IPSecProposalFilterSet


class IPSecPolicyViewSet(NetPointModelViewSet):
    queryset = IPSecPolicy.objects.all()
    serializer_class = serializers.IPSecPolicySerializer
    filterset_class = filtersets.IPSecPolicyFilterSet


class IPSecProfileViewSet(NetPointModelViewSet):
    queryset = IPSecProfile.objects.all()
    serializer_class = serializers.IPSecProfileSerializer
    filterset_class = filtersets.IPSecProfileFilterSet


class L2VPNViewSet(NetPointModelViewSet):
    queryset = L2VPN.objects.prefetch_related('import_targets', 'export_targets', 'tenant', 'tags')
    serializer_class = serializers.L2VPNSerializer
    filterset_class = filtersets.L2VPNFilterSet


class L2VPNTerminationViewSet(NetPointModelViewSet):
    queryset = L2VPNTermination.objects.prefetch_related('assigned_object')
    serializer_class = serializers.L2VPNTerminationSerializer
    filterset_class = filtersets.L2VPNTerminationFilterSet
