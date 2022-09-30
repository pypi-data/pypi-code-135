from typing import Generator
import uuid
import datetime as python_datetime
from decimal import Decimal
from django.http import JsonResponse as JsonResponseOriginal
from django.views import View


def all_subclasses(cls):
    for c in cls.__subclasses__():
        for s in all_subclasses(c):
            yield s
        yield c


def default_json(x):
    if isinstance(x, Generator):
        return [i for i in x]
    if isinstance(x, python_datetime.datetime):
        return str(x)
    if isinstance(x, python_datetime.date):
        return str(x)
    if isinstance(x, Decimal):
        return str(x)
    try:
        return str(x)
    except Exception as e:
        print(f"Don't know how to convert: {x} {type(x)}")
        return repr(x)


def JsonResponse(*args, **kwargs):
    kwargs["json_dumps_params"] = {"default": default_json}
    return JsonResponseOriginal(*args, **kwargs)


def media_upload(request):
    import base64
    from django.core.files.base import ContentFile
    from django.core.files.storage import default_storage

    body = request.POST  # json.loads(request.body)
    image_data = request.FILES["image"]
    # format, imgstr = image_data.split(';base64,')
    # print("format", format)
    ext = image_data.name.split(".")[-1]

    cfile = image_data  # ContentFile(base64.b64decode(imgstr))
    file_name = str(uuid.uuid4()) + "." + ext
    full_name = body["upload_to"] + file_name
    path = default_storage.save(full_name, cfile)
    return JsonResponse({"filename": path})


class ApiView(View):
    SHOULD_LOGIN_NOTIFICATION = {
        "type": "warning",
        "text": "Please, login or register",
    }

    def get(self, request, *args, **kwargs):
        user = None
        if not self.request.user.is_anonymous:
            user = {
                "id": self.request.user.id,
                "username": self.request.user.username,
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
                "email": self.request.user.email,
            }
        data = {
            "title": self.title,
            "wrapper": self.WRAPPER,
            "template": self.TEMPLATE,
            "user": user,
        }
        data.update(self.get_data(request, *args, **kwargs))
        return JsonResponse(data, safe=False)

    def should_login(self):
        return False

    def dispatch(self, request, *args, **kwargs):
        if self.should_login():
            return JsonResponse(
                {
                    "pushState": "/register",
                    "notification": self.SHOULD_LOGIN_NOTIFICATION,
                }
            )
        else:
            return super().dispatch(request, *args, **kwargs)

    def already_logged_in(self):
        if not self.request.user.is_anonymous:
            return {
                "pushState": self.request.GET.get("next", "/"),
                "notification": {
                    "type": "info",
                    "text": "You\'re already logged in",
                },
            }


def all_api_views():
    from django.urls import path
    for sc in all_subclasses(ApiView):
        if hasattr(sc, "url_path"):
            yield path(f"api{sc.url_path}", sc.as_view())
