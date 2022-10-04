from django.db import models


class ManagerReceivesUser(models.Manager):
    def filter(self, *args, **kwargs):
        self.user = kwargs.pop('request_user', None)
        return super(ManagerReceivesUser, self).filter(*args, **kwargs)
