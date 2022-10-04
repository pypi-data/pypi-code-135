from django.http import HttpRequest
from django.views import View

from ns.autoapi.decorators import handle_result, result_as_response
from ns.autoapi.entities import Request
from ns.autoapi.service import AutoapiService
from ns.di.injection import depends


class ApplicationDataView(View):
    service: AutoapiService = depends(AutoapiService)

    @result_as_response
    def get(self, request: HttpRequest):
        return self.service.get_application_data()


class ExecuteQuery(View):
    service: AutoapiService = depends(AutoapiService)

    @result_as_response
    @handle_result
    def get(self, request: HttpRequest, service_name: str, method_name: str):
        args = request.GET.dict()
        request_model = Request(
            service_name=service_name,
            method_name=method_name,
            args=args,
        )
        return self.service.execute_method(request_model)


class ExecuteMethod(View):
    service: AutoapiService = depends(AutoapiService)

    @result_as_response
    @handle_result
    def post(self, request: HttpRequest):
        request_data = request.POST.dict()
        request_model = Request(**request_data)
        return self.service.execute_method(request_model)
