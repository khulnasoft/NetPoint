import django_tables2 as tables
from django.utils.translation import gettext as _

from account.tables import UserTokenTable
from netpoint.tables import NetPointTable, columns
from users.models import NetPointGroup, NetPointUser, ObjectPermission, Token

__all__ = (
    'GroupTable',
    'ObjectPermissionTable',
    'TokenTable',
    'UserTable',
)


class TokenTable(UserTokenTable):
    user = tables.Column(
        linkify=True,
        verbose_name=_('User')
    )

    class Meta(NetPointTable.Meta):
        model = Token
        fields = (
            'pk', 'id', 'key', 'user', 'description', 'write_enabled', 'created', 'expires', 'last_used', 'allowed_ips',
        )


class UserTable(NetPointTable):
    username = tables.Column(
        verbose_name=_('Username'),
        linkify=True
    )
    groups = columns.ManyToManyColumn(
        verbose_name=_('Groups'),
        linkify_item=('users:netpointgroup', {'pk': tables.A('pk')})
    )
    is_active = columns.BooleanColumn(
        verbose_name=_('Is Active'),
    )
    is_staff = columns.BooleanColumn(
        verbose_name=_('Is Staff'),
    )
    is_superuser = columns.BooleanColumn(
        verbose_name=_('Is Superuser'),
    )
    actions = columns.ActionsColumn(
        actions=('edit', 'delete'),
    )

    class Meta(NetPointTable.Meta):
        model = NetPointUser
        fields = (
            'pk', 'id', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_staff',
            'is_superuser', 'last_login',
        )
        default_columns = ('pk', 'username', 'first_name', 'last_name', 'email', 'is_active')


class GroupTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    actions = columns.ActionsColumn(
        actions=('edit', 'delete'),
    )

    class Meta(NetPointTable.Meta):
        model = NetPointGroup
        fields = (
            'pk', 'id', 'name', 'users_count',
        )
        default_columns = ('pk', 'name', 'users_count', )


class ObjectPermissionTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    object_types = columns.ContentTypesColumn(
        verbose_name=_('Object Types'),
    )
    enabled = columns.BooleanColumn(
        verbose_name=_('Enabled'),
    )
    can_view = columns.BooleanColumn(
        verbose_name=_('Can View'),
    )
    can_add = columns.BooleanColumn(
        verbose_name=_('Can Add'),
    )
    can_change = columns.BooleanColumn(
        verbose_name=_('Can Change'),
    )
    can_delete = columns.BooleanColumn(
        verbose_name=_('Can Delete'),
    )
    custom_actions = columns.ArrayColumn(
        verbose_name=_('Custom Actions'),
        accessor=tables.A('actions')
    )
    users = columns.ManyToManyColumn(
        verbose_name=_('Users'),
        linkify_item=('users:netpointuser', {'pk': tables.A('pk')})
    )
    groups = columns.ManyToManyColumn(
        verbose_name=_('Groups'),
        linkify_item=('users:netpointgroup', {'pk': tables.A('pk')})
    )
    actions = columns.ActionsColumn(
        actions=('edit', 'delete'),
    )

    class Meta(NetPointTable.Meta):
        model = ObjectPermission
        fields = (
            'pk', 'id', 'name', 'enabled', 'object_types', 'can_view', 'can_add', 'can_change', 'can_delete',
            'custom_actions', 'users', 'groups', 'constraints', 'description',
        )
        default_columns = (
            'pk', 'name', 'enabled', 'object_types', 'can_view', 'can_add', 'can_change', 'can_delete', 'description',
        )
