from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        ...