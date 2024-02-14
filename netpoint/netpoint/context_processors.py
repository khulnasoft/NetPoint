from django.conf import settings as django_settings

from netpoint.config import get_config
from netpoint.registry import registry


def settings_and_registry(request):
    """
    Expose Django settings and NetPoint registry stores in the template context. Example: {{ settings.DEBUG }}
    """
    return {
        'settings': django_settings,
        'config': get_config(),
        'registry': registry,
        'preferences': request.user.config if request.user.is_authenticated else {},
    }
