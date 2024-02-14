from django.utils.translation import gettext_lazy as _
import django_tables2 as tables
from django_tables2.utils import Accessor

from netpoint.tables import NetPointTable, columns
from tenancy.models import *
from utilities.tables import linkify_phone

__all__ = (
    'ContactAssignmentTable',
    'ContactGroupTable',
    'ContactRoleTable',
    'ContactTable',
)


class ContactGroupTable(NetPointTable):
    name = columns.MPTTColumn(
        verbose_name=_('Name'),
        linkify=True
    )
    contact_count = columns.LinkedCountColumn(
        viewname='tenancy:contact_list',
        url_params={'group_id': 'pk'},
        verbose_name=_('Contacts')
    )
    tags = columns.TagColumn(
        url_name='tenancy:contactgroup_list'
    )

    class Meta(NetPointTable.Meta):
        model = ContactGroup
        fields = (
            'pk', 'name', 'contact_count', 'description', 'slug', 'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = ('pk', 'name', 'contact_count', 'description')


class ContactRoleTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    tags = columns.TagColumn(
        url_name='tenancy:contactrole_list'
    )

    class Meta(NetPointTable.Meta):
        model = ContactRole
        fields = ('pk', 'name', 'description', 'slug', 'tags', 'created', 'last_updated', 'actions')
        default_columns = ('pk', 'name', 'description')


class ContactTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    group = tables.Column(
        verbose_name=_('Group'),
        linkify=True
    )
    phone = tables.Column(
        verbose_name=_('Phone'),
        linkify=linkify_phone,
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    assignment_count = columns.LinkedCountColumn(
        viewname='tenancy:contactassignment_list',
        url_params={'contact_id': 'pk'},
        verbose_name=_('Assignments')
    )
    tags = columns.TagColumn(
        url_name='tenancy:contact_list'
    )

    class Meta(NetPointTable.Meta):
        model = Contact
        fields = (
            'pk', 'name', 'group', 'title', 'phone', 'email', 'address', 'link', 'description', 'comments',
            'assignment_count', 'tags', 'created', 'last_updated',
        )
        default_columns = ('pk', 'name', 'group', 'assignment_count', 'title', 'phone', 'email')


class ContactAssignmentTable(NetPointTable):
    content_type = columns.ContentTypeColumn(
        verbose_name=_('Object Type')
    )
    object = tables.Column(
        verbose_name=_('Object'),
        linkify=True,
        orderable=False
    )
    contact = tables.Column(
        verbose_name=_('Contact'),
        linkify=True
    )
    role = tables.Column(
        verbose_name=_('Role'),
        linkify=True
    )
    contact_group = tables.Column(
        accessor=Accessor('contact__group'),
        verbose_name=_('Group'),
        linkify=True
    )
    contact_title = tables.Column(
        accessor=Accessor('contact__title'),
        verbose_name=_('Contact Title')
    )
    contact_phone = tables.Column(
        accessor=Accessor('contact__phone'),
        verbose_name=_('Contact Phone')
    )
    contact_email = tables.Column(
        accessor=Accessor('contact__email'),
        verbose_name=_('Contact Email')
    )
    contact_address = tables.Column(
        accessor=Accessor('contact__address'),
        verbose_name=_('Contact Address')
    )
    contact_link = tables.Column(
        accessor=Accessor('contact__link'),
        verbose_name=_('Contact Link')
    )
    contact_description = tables.Column(
        accessor=Accessor('contact__description'),
        verbose_name=_('Contact Description')
    )
    tags = columns.TagColumn(
        url_name='tenancy:contactassignment_list'
    )
    actions = columns.ActionsColumn(
        actions=('edit', 'delete')
    )

    class Meta(NetPointTable.Meta):
        model = ContactAssignment
        fields = (
            'pk', 'content_type', 'object', 'contact', 'role', 'priority', 'contact_title', 'contact_phone',
            'contact_email', 'contact_address', 'contact_link', 'contact_description', 'contact_group', 'tags',
            'actions'
        )
        default_columns = (
            'pk', 'content_type', 'object', 'contact', 'role', 'priority', 'contact_email', 'contact_phone'
        )
