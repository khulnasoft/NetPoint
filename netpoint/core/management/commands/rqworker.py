import logging

from django_rq.management.commands.rqworker import Command as _Command


DEFAULT_QUEUES = ('high', 'default', 'low')

logger = logging.getLogger('netpoint.rqworker')


class Command(_Command):
    """
    Subclass django_rq's built-in rqworker to listen on all configured queues if none are specified (instead
    of only the 'default' queue).
    """
    def handle(self, *args, **options):
        # Run the worker with scheduler functionality
        options['with_scheduler'] = True

        # If no queues have been specified on the command line, listen on all configured queues.
        if len(args) < 1:
            queues = ', '.join(DEFAULT_QUEUES)
            logger.warning(
                f"No queues have been specified. This process will service the following queues by default: {queues}"
            )
            args = DEFAULT_QUEUES

        super().handle(*args, **options)
