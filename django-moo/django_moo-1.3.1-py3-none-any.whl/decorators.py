import inspect
from functools import wraps
from django.http import HttpResponse, JsonResponse
from django.db.models.query import QuerySet
from django.db.models import Model
from django.http.response import HttpResponseBase
from django.template import TemplateDoesNotExist
from django.shortcuts import render
from .utils import QToDict, rest_response

def url_pattern(url_path, isregex=False, **kwargs):  # url_path, isregex, name(template_name)
    def middle(func):
        @wraps(func)
        def inner(request, *args, **innerkwargs):
            result = func(request, *args, **innerkwargs)
            return result
        if not hasattr(url_pattern, "_all_func"):
            url_pattern._all_func = []
        context = {}
        context['url_path'] = url_path
        context['isregex'] = isregex
        context['func'] = func
        context['name'] = kwargs.get('name') or func.__name__
        url_pattern._all_func.append(context)
        return inner
    return middle

def rest_controller(func):
    @wraps(func)
    def deal(request):
        result = func(request)
        if result is None:
            return result
        elif isinstance(result, dict):
            return rest_response(result)
        elif isinstance(result, Model) or isinstance(result, QuerySet):
            data = QToDict(result, request).get_result()
            return rest_response(data)
        elif isinstance(result, HttpResponseBase):
            return result
        elif isinstance(result, (set,list)):
            return rest_response(list(result))
        elif isinstance(result, str):
            return rest_response(result)
        else:
            return HttpResponse(result)
    return deal

def controller(func):
    @wraps(func)
    def deal(request, *args, **kwargs):
        context = func(request, *args, **kwargs)
        _package = inspect.getfile(func).split('\\')[-2]
        template_name = _package + '/' + func.__name__ + ".html"
        if isinstance(context, dict):
            try:
                return render(request, template_name, context)
            except TemplateDoesNotExist:
                return HttpResponse("缺少html文件！")
        if isinstance(context, QuerySet) or isinstance(context, Model):
            try:
                return render(request, template_name, {"ones":context})
            except TemplateDoesNotExist:
                return HttpResponse("缺少html文件！")
        if hasattr(context, '_meta') and callable(context):
            try:
                return render(request, template_name, {"ones":context._default_manager.all()})
            except TemplateDoesNotExist:
                return HttpResponse("缺少html文件！")
        if context is None:
            return HttpResponse("")
        if isinstance(context, HttpResponseBase):
            return context
        return HttpResponse(str(context))
    return deal
