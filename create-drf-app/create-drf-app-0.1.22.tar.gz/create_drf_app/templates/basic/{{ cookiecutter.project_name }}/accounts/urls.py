from xml.etree.ElementInclude import include
from django.urls import path

from accounts.views import CreateAccountView

from rest_framework import routers

from accounts.views import  WhoamiViewSet

router = routers.DefaultRouter()

router.register(r'whoami', WhoamiViewSet, basename="whoami")

urlpatterns = [
    path('signup/', CreateAccountView.as_view()),
    path('', include(router.urls))
]