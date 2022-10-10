from django.urls import path
from . import views

app_name = 'niceadmin'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:title>/<str:subtitle>/', views.examples, name='examples'),
]
