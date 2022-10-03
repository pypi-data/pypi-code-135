from django.conf import settings

auth_app_name, auth_user_model = settings.AUTH_USER_MODEL.split(".")
