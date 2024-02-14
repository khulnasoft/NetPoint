from django.utils.translation import gettext_lazy as _

from core.models import ConfigRevision
from netpoint.tables import NetPointTable, columns

__all__ = (
    'ConfigRevisionTable',
)

REVISION_BUTTONS = """
{% if not record.is_active %}
<a href="{% url 'core:configrevision_restore' pk=record.pk %}" class="btn btn-sm btn-primary" title="Restore config">
    <i class="mdi mdi-file-restore"></i>
</a>
{% endif %}
"""


class ConfigRevisionTable(NetPointTable):
    is_active = columns.BooleanColumn(
        verbose_name=_('Is Active'),
    )
    actions = columns.ActionsColumn(
        actions=('delete',),
        extra_buttons=REVISION_BUTTONS
    )

    class Meta(NetPointTable.Meta):
        model = ConfigRevision
        fields = (
            'pk', 'id', 'is_active', 'created', 'comment',
        )
        default_columns = ('pk', 'id', 'is_active', 'created', 'comment')
