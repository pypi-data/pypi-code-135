# #-*-coding: utf-8 -*-
# """ Celery Settings."""
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings
# from navigator.settings.settings import CELERY_REDIS_DB, CELERY_BROKER_URL

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'navigator.settings.settings')

# app = Celery('troc')
# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.update(
#     BROKER_URL = CELERY_BROKER_URL,
# )
# # configuration of broker
# app.conf.broker_url = CELERY_BROKER_URL + '/' + str(CELERY_REDIS_DB)

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     """Sample Task Debugging."""
#     print('Request: {0!r}'.format(self.request))
