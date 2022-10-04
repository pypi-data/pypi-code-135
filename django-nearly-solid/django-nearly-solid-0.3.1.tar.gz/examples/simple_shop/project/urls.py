from django.contrib import admin
from django.urls import path

from ns.autoapi.urls import urlpatterns as autoapi_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
] + autoapi_urlpatterns
