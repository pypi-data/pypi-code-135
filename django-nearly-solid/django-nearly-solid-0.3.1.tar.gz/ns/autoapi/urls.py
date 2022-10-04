from django.urls import path

from ns.autoapi import views


urlpatterns = [
    path('application_data/', views.ApplicationDataView.as_view()),
    path('execute_method/', views.ExecuteMethod.as_view()),
]
