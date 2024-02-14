import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netpoint.tables import NetPointTable, columns
from vpn.models import *

__all__ = (
    'IKEPolicyTable',
    'IKEProposalTable',
    'IPSecPolicyTable',
    'IPSecProposalTable',
    'IPSecProfileTable',
)


class IKEProposalTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    authentication_method = tables.Column(
        verbose_name=_('Authentication Method')
    )
    encryption_algorithm = tables.Column(
        verbose_name=_('Encryption Algorithm')
    )
    authentication_algorithm = tables.Column(
        verbose_name=_('Authentication Algorithm')
    )
    group = tables.Column(
        verbose_name=_('Group')
    )
    sa_lifetime = tables.Column(
        verbose_name=_('SA Lifetime')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='vpn:ikeproposal_list'
    )

    class Meta(NetPointTable.Meta):
        model = IKEProposal
        fields = (
            'pk', 'id', 'name', 'authentication_method', 'encryption_algorithm', 'authentication_algorithm',
            'group', 'sa_lifetime', 'description', 'comments', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'name', 'authentication_method', 'encryption_algorithm', 'authentication_algorithm', 'group',
            'sa_lifetime', 'description',
        )


class IKEPolicyTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    version = tables.Column(
        verbose_name=_('Version')
    )
    mode = tables.Column(
        verbose_name=_('Mode')
    )
    proposals = tables.ManyToManyColumn(
        linkify_item=True,
        verbose_name=_('Proposals')
    )
    preshared_key = tables.Column(
        verbose_name=_('Pre-shared Key')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='vpn:ikepolicy_list'
    )

    class Meta(NetPointTable.Meta):
        model = IKEPolicy
        fields = (
            'pk', 'id', 'name', 'version', 'mode', 'proposals', 'preshared_key', 'description', 'comments', 'tags',
            'created', 'last_updated',
        )
        default_columns = (
            'pk', 'name', 'version', 'mode', 'proposals', 'description',
        )


class IPSecProposalTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    encryption_algorithm = tables.Column(
        verbose_name=_('Encryption Algorithm')
    )
    authentication_algorithm = tables.Column(
        verbose_name=_('Authentication Algorithm')
    )
    sa_lifetime_seconds = tables.Column(
        verbose_name=_('SA Lifetime (Seconds)')
    )
    sa_lifetime_data = tables.Column(
        verbose_name=_('SA Lifetime (KB)')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='vpn:ipsecproposal_list'
    )

    class Meta(NetPointTable.Meta):
        model = IPSecProposal
        fields = (
            'pk', 'id', 'name', 'encryption_algorithm', 'authentication_algorithm', 'sa_lifetime_seconds',
            'sa_lifetime_data', 'description', 'comments', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'name', 'encryption_algorithm', 'authentication_algorithm', 'sa_lifetime_seconds',
            'sa_lifetime_data', 'description',
        )


class IPSecPolicyTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    proposals = tables.ManyToManyColumn(
        linkify_item=True,
        verbose_name=_('Proposals')
    )
    pfs_group = tables.Column(
        verbose_name=_('PFS Group')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='vpn:ipsecpolicy_list'
    )

    class Meta(NetPointTable.Meta):
        model = IPSecPolicy
        fields = (
            'pk', 'id', 'name', 'proposals', 'pfs_group', 'description', 'comments', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'name', 'proposals', 'pfs_group', 'description',
        )


class IPSecProfileTable(NetPointTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    mode = tables.Column(
        verbose_name=_('Mode')
    )
    ike_policy = tables.Column(
        linkify=True,
        verbose_name=_('IKE Policy')
    )
    ipsec_policy = tables.Column(
        linkify=True,
        verbose_name=_('IPSec Policy')
    )
    comments = columns.MarkdownColumn(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='vpn:ipsecprofile_list'
    )

    class Meta(NetPointTable.Meta):
        model = IPSecProfile
        fields = (
            'pk', 'id', 'name', 'mode', 'ike_policy', 'ipsec_policy', 'description', 'comments', 'tags', 'created',
            'last_updated',
        )
        default_columns = ('pk', 'name', 'mode', 'ike_policy', 'ipsec_policy', 'description')
