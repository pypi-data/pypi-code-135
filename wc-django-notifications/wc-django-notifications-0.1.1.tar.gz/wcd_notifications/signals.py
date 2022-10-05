from django.dispatch import Signal


notification_sended = Signal()
notifications_sended = Signal()
notifications_flags_changed = Signal()
notifications_updated = Signal()
notifications_cleared = Signal()

stats_updated = Signal()
