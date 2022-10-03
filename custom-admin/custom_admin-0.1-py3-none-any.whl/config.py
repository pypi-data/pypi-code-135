from django.conf import settings

settings_var_possibilities = ["SUIT_CONFIG", "CUSTOM_ADMIN_CONFIG", "ADMIN_CONFIG"]

BASE_CUSTOM_ADMIN_CONFIG = {
    "ADMIN_NAME": "Admin",
    "HEADER_DATE_FORMAT": "l, F j Y",
    "HEADER_TIME_FORMAT": "h:i A",
    "SHOW_DJANGO_SIDEBAR": False,
    "MENU": (
        {"label": "Django", "icon": "fas fa-gear", "app": "django.contrib.admin"},
        {"label": "Django", "icon": "fas fa-gear", "app": "django.contrib.auth"},
        {"label": "Custom Admin", "icon": "fas fa-gear", "app": "custom_admin"},
    ),
}
CUSTOM_ADMIN_CONFIG = None
for settings_var_possibility in settings_var_possibilities:
    if hasattr(settings, settings_var_possibility):
        CUSTOM_ADMIN_CONFIG = getattr(settings, settings_var_possibility)

if CUSTOM_ADMIN_CONFIG is None:
    CUSTOM_ADMIN_CONFIG = BASE_CUSTOM_ADMIN_CONFIG
