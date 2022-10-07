from rest_framework.views import APIView

from dry_django.contrib.rest_framework.mixins import ApiDefaultMixin


class DefaultAPIView(ApiDefaultMixin, APIView):
    """
    Базовый класс для создания представлений, включающий миксины по умолчанию
    """

    pass
