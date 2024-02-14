from core import filtersets, models
from netpoint.graphql.types import BaseObjectType, NetPointObjectType

__all__ = (
    'DataFileType',
    'DataSourceType',
)


class DataFileType(BaseObjectType):
    class Meta:
        model = models.DataFile
        exclude = ('data',)
        filterset_class = filtersets.DataFileFilterSet


class DataSourceType(NetPointObjectType):
    class Meta:
        model = models.DataSource
        fields = '__all__'
        filterset_class = filtersets.DataSourceFilterSet
