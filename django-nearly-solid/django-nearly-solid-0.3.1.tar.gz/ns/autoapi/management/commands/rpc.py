from django.core.management.commands.runserver import Command as RunServerCommand


class Command(RunServerCommand):
    def handle(self, *args, **options):
        # gevent.monkey.patch_all()
        super().handle(*args, **options)
