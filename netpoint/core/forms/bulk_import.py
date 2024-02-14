from core.models import *
from netpoint.forms import NetPointModelImportForm

__all__ = (
    'DataSourceImportForm',
)


class DataSourceImportForm(NetPointModelImportForm):

    class Meta:
        model = DataSource
        fields = (
            'name', 'type', 'source_url', 'enabled', 'description', 'comments', 'parameters', 'ignore_rules',
        )
