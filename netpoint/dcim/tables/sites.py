from django.utils.translation import gettext_lazy as _
import django_tables2 as tables
from dcim.models import Location, Region, Site, SiteGroup
from tenancy.tables import ContactsColumnMixin, TenancyColumnsMixin

from netpoint.tables import NetPointTable, columns

from .template_code import LOCATION_BUTTONS

__all__ = (
    'LocationTable',
    'RegionTable',
    'SiteTable',
    'SiteGroupTable',
)


#
# Regions
#

class RegionTable(ContactsColumnMixin, NetPointTable):
    name = columns.MPTTColumn(
        verbose_name=_('Name'),
        linkify=True
    )
    site_count = columns.LinkedCountColumn(
        viewname='dcim:site_list',
        url_params={'region_id': 'pk'},
        verbose_name=_('Sites')
    )
    tags = columns.TagColumn(
        url_name='dcim:region_list'
    )

    class Meta(NetPointTable.Meta):
        model = Region
        fields = (
            'pk', 'id', 'name', 'slug', 'site_count', 'description', 'contacts', 'tags', 'created', 'last_updated',
            'actions',
        )
        default_columns = ('pk', 'name', 'site_count', 'description')


#
# Site groups
#

class SiteGroupTable(ContactsColumnMixin, NetPointTable):
    name = columns.MPTTColumn(
        verbose_name=_('Name'),
        linkify=True
    )
    site_count = columns.LinkedCountColumn(
        viewname='dcim:site_list',
        url_params={'group_id': 'pk'},
        verbose_name=_('Sites')
    )
    tags = columns.TagColumn(
        url_name='dcim:sitegroup_list'
    )

    class Meta(NetPointTable.Meta):
        model = SiteGroup
        fields = (
            'pk', 'id', 'name', 'slug', 'site_count', 'description', 'contacts', 'tags', 'created', 'last_updated',
            'actions',
        )
        default_columns = ('pk', 'name', 'site_count', 'description')


#
# Sites
#

class SiteTable(TenancyColumnsMixin, ContactsColumnMixin, NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    region = tables.Column(
        verbose_name=_('Region'),
        linkify=True
    )
    group = tables.Column(
        verbose_name=_('Group'),
        linkify=True
    )
    asns = columns.ManyToManyColumn(
        linkify_item=True,
        verbose_name=_('ASNs')
    )
    asn_count = columns.LinkedCountColumn(
        accessor=tables.A('asns__count'),
        viewname='ipam:asn_list',
        url_params={'site_id': 'pk'},
        verbose_name=_('ASN Count')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='dcim:site_list'
    )

    class Meta(NetPointTable.Meta):
        model = Site
        fields = (
            'pk', 'id', 'name', 'slug', 'status', 'facility', 'region', 'group', 'tenant', 'tenant_group', 'asns',
            'asn_count', 'time_zone', 'description', 'physical_address', 'shipping_address', 'latitude', 'longitude',
            'comments', 'contacts', 'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = ('pk', 'name', 'status', 'facility', 'region', 'group', 'tenant', 'description')


#
# Locations
#

class LocationTable(TenancyColumnsMixin, ContactsColumnMixin, NetPointTable):
    name = columns.MPTTColumn(
        verbose_name=_('Name'),
        linkify=True
    )
    site = tables.Column(
        verbose_name=_('Site'),
        linkify=True
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    rack_count = columns.LinkedCountColumn(
        viewname='dcim:rack_list',
        url_params={'location_id': 'pk'},
        verbose_name=_('Racks')
    )
    device_count = columns.LinkedCountColumn(
        viewname='dcim:device_list',
        url_params={'location_id': 'pk'},
        verbose_name=_('Devices')
    )
    tags = columns.TagColumn(
        url_name='dcim:location_list'
    )
    actions = columns.ActionsColumn(
        extra_buttons=LOCATION_BUTTONS
    )

    class Meta(NetPointTable.Meta):
        model = Location
        fields = (
            'pk', 'id', 'name', 'site', 'status', 'tenant', 'tenant_group', 'rack_count', 'device_count', 'description',
            'slug', 'contacts', 'tags', 'actions', 'created', 'last_updated',
        )
        default_columns = ('pk', 'name', 'site', 'status', 'tenant', 'rack_count', 'device_count', 'description')
