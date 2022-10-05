from django.contrib import admin

from .models import Notification, Stats
from .services import manager


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = 'id', 'message', 'recipient', 'created_at',
    list_filter = (
        'recipient_content_type', 'actor_content_type',
        'action_content_type', 'target_content_type',
    )
    search_fields = (
        'recipient_content_type', 'recipient_object_id',
        'actor_content_type', 'actor_object_id',
        'action_content_type', 'action_object_id',
        'target_content_type', 'target_object_id',
        'flags', 'message', 'data',
    )

    def save_model(self, request, obj, form, change) -> None:
        result = super().save_model(request, obj, form, change)

        manager.collect_stats([obj.recipient])

        return result


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = 'id', 'recipient', 'total',
    list_filter = 'recipient_content_type',
    search_fields = (
        'recipient_content_type', 'recipient_object_id',
        'flags', 'total',
    )
