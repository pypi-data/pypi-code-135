from django.dispatch import receiver

from .signals import (
    notifications_sended, notifications_updated, notifications_cleared,
)
from .services import manager


@receiver(notifications_sended)
@receiver(notifications_updated)
@receiver(notifications_cleared)
def update_stats_on_notifications_change(sender, instances, **kw):
    recipients = {x.recipient for x in instances}

    if len(recipients) > 0:
        manager.collect_stats(recipients)
