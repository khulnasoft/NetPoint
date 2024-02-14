from wireless import filtersets, models
from netpoint.graphql.types import OrganizationalObjectType, NetPointObjectType

__all__ = (
    'WirelessLANType',
    'WirelessLANGroupType',
    'WirelessLinkType',
)


class WirelessLANGroupType(OrganizationalObjectType):

    class Meta:
        model = models.WirelessLANGroup
        fields = '__all__'
        filterset_class = filtersets.WirelessLANGroupFilterSet


class WirelessLANType(NetPointObjectType):

    class Meta:
        model = models.WirelessLAN
        fields = '__all__'
        filterset_class = filtersets.WirelessLANFilterSet

    def resolve_auth_type(self, info):
        return self.auth_type or None

    def resolve_auth_cipher(self, info):
        return self.auth_cipher or None


class WirelessLinkType(NetPointObjectType):

    class Meta:
        model = models.WirelessLink
        fields = '__all__'
        filterset_class = filtersets.WirelessLinkFilterSet

    def resolve_auth_type(self, info):
        return self.auth_type or None

    def resolve_auth_cipher(self, info):
        return self.auth_cipher or None
