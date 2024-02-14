import graphene

from circuits import filtersets, models
from dcim.graphql.mixins import CabledObjectMixin
from extras.graphql.mixins import CustomFieldsMixin, TagsMixin, ContactsMixin
from netpoint.graphql.types import ObjectType, OrganizationalObjectType, NetPointObjectType

__all__ = (
    'CircuitTerminationType',
    'CircuitType',
    'CircuitTypeType',
    'ProviderType',
    'ProviderAccountType',
    'ProviderNetworkType',
)


class CircuitTerminationType(CustomFieldsMixin, TagsMixin, CabledObjectMixin, ObjectType):

    class Meta:
        model = models.CircuitTermination
        fields = '__all__'
        filterset_class = filtersets.CircuitTerminationFilterSet


class CircuitType(NetPointObjectType, ContactsMixin):
    class Meta:
        model = models.Circuit
        fields = '__all__'
        filterset_class = filtersets.CircuitFilterSet


class CircuitTypeType(OrganizationalObjectType):

    class Meta:
        model = models.CircuitType
        fields = '__all__'
        filterset_class = filtersets.CircuitTypeFilterSet


class ProviderType(NetPointObjectType, ContactsMixin):

    class Meta:
        model = models.Provider
        fields = '__all__'
        filterset_class = filtersets.ProviderFilterSet


class ProviderAccountType(NetPointObjectType):

    class Meta:
        model = models.ProviderAccount
        fields = '__all__'
        filterset_class = filtersets.ProviderAccountFilterSet


class ProviderNetworkType(NetPointObjectType):

    class Meta:
        model = models.ProviderNetwork
        fields = '__all__'
        filterset_class = filtersets.ProviderNetworkFilterSet
