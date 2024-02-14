from django.apps import AppConfig

from netpoint import denormalized


class VirtualizationConfig(AppConfig):
    name = 'virtualization'

    def ready(self):
        from . import search, signals
        from .models import VirtualMachine
        from utilities.counters import connect_counters

        # Register denormalized fields
        denormalized.register(VirtualMachine, 'cluster', {
            'site': 'site',
        })

        # Register counters
        connect_counters(VirtualMachine)
