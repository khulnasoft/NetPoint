from django import forms
from django.utils.translation import gettext_lazy as _

from netpoint.forms import NetPointModelForm
from tenancy.models import *
from utilities.forms.fields import CommentField, DynamicModelChoiceField, SlugField

__all__ = (
    'ContactAssignmentForm',
    'ContactForm',
    'ContactGroupForm',
    'ContactRoleForm',
    'TenantForm',
    'TenantGroupForm',
)


#
# Tenants
#

class TenantGroupForm(NetPointModelForm):
    parent = DynamicModelChoiceField(
        label=_('Parent'),
        queryset=TenantGroup.objects.all(),
        required=False
    )
    slug = SlugField()

    fieldsets = (
        (_('Tenant Group'), (
            'parent', 'name', 'slug', 'description', 'tags',
        )),
    )

    class Meta:
        model = TenantGroup
        fields = [
            'parent', 'name', 'slug', 'description', 'tags',
        ]


class TenantForm(NetPointModelForm):
    slug = SlugField()
    group = DynamicModelChoiceField(
        label=_('Group'),
        queryset=TenantGroup.objects.all(),
        required=False
    )
    comments = CommentField()

    fieldsets = (
        (_('Tenant'), ('name', 'slug', 'group', 'description', 'tags')),
    )

    class Meta:
        model = Tenant
        fields = (
            'name', 'slug', 'group', 'description', 'comments', 'tags',
        )


#
# Contacts
#

class ContactGroupForm(NetPointModelForm):
    parent = DynamicModelChoiceField(
        label=_('Parent'),
        queryset=ContactGroup.objects.all(),
        required=False
    )
    slug = SlugField()

    fieldsets = (
        (_('Contact Group'), (
            'parent', 'name', 'slug', 'description', 'tags',
        )),
    )

    class Meta:
        model = ContactGroup
        fields = ('parent', 'name', 'slug', 'description', 'tags')


class ContactRoleForm(NetPointModelForm):
    slug = SlugField()

    fieldsets = (
        (_('Contact Role'), (
            'name', 'slug', 'description', 'tags',
        )),
    )

    class Meta:
        model = ContactRole
        fields = ('name', 'slug', 'description', 'tags')


class ContactForm(NetPointModelForm):
    group = DynamicModelChoiceField(
        label=_('Group'),
        queryset=ContactGroup.objects.all(),
        required=False
    )
    comments = CommentField()

    fieldsets = (
        (_('Contact'), ('group', 'name', 'title', 'phone', 'email', 'address', 'link', 'description', 'tags')),
    )

    class Meta:
        model = Contact
        fields = (
            'group', 'name', 'title', 'phone', 'email', 'address', 'link', 'description', 'comments', 'tags',
        )
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class ContactAssignmentForm(NetPointModelForm):
    group = DynamicModelChoiceField(
        label=_('Group'),
        queryset=ContactGroup.objects.all(),
        required=False,
        initial_params={
            'contacts': '$contact'
        }
    )
    contact = DynamicModelChoiceField(
        label=_('Contact'),
        queryset=Contact.objects.all(),
        query_params={
            'group_id': '$group'
        }
    )
    role = DynamicModelChoiceField(
        label=_('Role'),
        queryset=ContactRole.objects.all()
    )

    class Meta:
        model = ContactAssignment
        fields = (
            'content_type', 'object_id', 'group', 'contact', 'role', 'priority', 'tags'
        )
        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
        }
