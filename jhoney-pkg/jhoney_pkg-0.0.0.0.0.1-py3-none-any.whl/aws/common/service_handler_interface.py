# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta
from .paginator import Paginator


class ServiceHandlerInterface(metaclass=ABCMeta):
    shared_dict = None
    session = None
    client = None
    vpc = None
    isGlobalService = None
    cloudwatch_namespaces = None
    aws_account_id = None
    aws_connect_key_dict = None

    def __init__(self, session_, shared_dict_, aws_account_id_, aws_connect_key_dict_):
        self.shared_dict = shared_dict_
        self.session = session_
        self.client_setting()
        self.vpc = "vpc"
        self.isGlobalService = False
        self.aws_account_id = aws_account_id_
        self.aws_connect_key_dict = aws_connect_key_dict_
        self.init_add()

    def client_setting(self):
        self.client = self.get_aws_client()

    def init_add(self):
        pass

    @classmethod
    @abstractmethod
    def get_service_name(cls):
        pass

    @classmethod
    @abstractmethod
    def get_dependencies(cls):
        pass

    # 본인의 세션으로부터 aws client 를 반환합니다.
    def get_aws_client(self, service=None):
        """
        본인의 세션으로부터 aws client 를 반환합니다.
        - service 값의 Default 값은 None이며, None이면 본인의 서비스 이름을 바탕으로, client 를 반환합니다.
        - service 값에 별도로 이름을 넣으면 해당 서비스의 client 를 반환합니다.
        """
        client = None
        if service is None:
            service = self.get_service_name()
        try:
            client = self.session.client(service)
        except:
            pass
        return client

    def client_method_describe(self, func_name: str, *, service: str = None, allpages: bool = True, metaData: bool = False, **params: dict) -> list or dict:
        """
        해당 서비스의 client에 대해서, func_name: str 이름의 함수에 매개변수 Key=Value,... 형식의 **params를 부여해서 메소드를 호출하고 반환한다.
        - service 의 Default 값은 None 이며, 이 경우 해당 서비스에 선언된 client로 호출한다.
            - 별도로 호출하면, 그 service의 client로 연결한다.
        - allpages 의 Default 값은 True로, Next 반복문을 돌아서 끝까지 모두 호출후에 반환한다.
            - False 이면, 끝까지 반복하지 않고 1번만 수행한 값을 반환한다.
        - metaData 의 Default 값은 False 이며, list 값을 반환한다.
            - True 이면, MetaData를 포함시켜서 dict 값을 반환한다.
        """
        # print(f" func: {func_name!r} \n metaData: {metaData!r} \n allpages: {allpages!r} \n params: {params!r} \n")
        if service is None:
            func = getattr(self.client, func_name)
        else:
            func = getattr(self.session.client(service), func_name)
        response = Paginator.describe_allpages(func, metaData=metaData, allpages=allpages, **params)

        return response
