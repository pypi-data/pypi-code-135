from django.contrib import admin

from custom_admin.models import ExceptionLog

@admin.register(EmailRecipient)
class EmailRecipientAdmin(admin.ModelAdmin):
    list_display = ("email", "enabled",)
    search_fields = ("email",)
    filter_vertical = ("reports",)


@admin.register(EmailReport)
class EmailReportAdmin(admin.ModelAdmin):
    list_display = ("report_name", "enabled")
    fields = ("enabled", "report_name", "recipients_inline",)
    readonly_fields = ("recipients_inline",)

@admin.register(ExceptionLog)
class ExceptionLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "path")
    fields = (
        "timestamp",
        "troubleshooter_link",
        "path",
        "filename",
        "function_name",
        "line_number",
        "message",
        "exception",
        "formatted_traceback",
    )
    readonly_fields = (
        "timestamp",
        "troubleshooter_link",
        "path",
        "filename",
        "function_name",
        "line_number",
        "exception",
        "formatted_traceback",
    )
    list_filter = ("path", "function_name", "filename")
    search_fields = ("user__username", "user__email", "exception", "function_name")
