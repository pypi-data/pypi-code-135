#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import os
from .common import *


class AwsSupporter:
    """
    aws_supporter.py

    """

    aws_account_id = None  # AWS 계정 ID
    region_name = None  # AWS 리전 이름
    session = None  # 연결된 AWS Session
    account_name = None  # AWS 계정의 이름. 실질적으로 사용은 안됨
    # alias = None  # AWS 계정의 alias
    support_plan_level = None  # AWS 계정의 Support Plan
    shared_dict = None  # 모든 서비스들이 공유하는 dictinary
    service_dict = None  # ServiceHandlerInterface 하위 클래스를 Service 이름과 instance를 매칭한 dictinary

    # 생성자 함수
    def __init__(self, account_name: str = None, region_name: str = "ap-northeast-2", **aws_connect_key_dict: dict) -> None:
        self.region_name = region_name
        self.aws_connect_key_dict = aws_connect_key_dict

        self.session = connect_aws_session(region_name=region_name, **aws_connect_key_dict)
        if region_name != "us-east-1":
            self.global_session = connect_aws_session(region_name="us-east-1", **aws_connect_key_dict)
        else:
            self.global_session = self.session
        # print("self.session:", self.session)
        self.account_name = account_name
        if account_name is None:
            self.account_name = get_account_alias(self.session)
        self.aws_account_id = get_aws_account_id(self.session)
        self.support_plan_level = get_aws_support_plan_level(self.global_session)
        self.shared_dict = dict()
        self.service_dict = dict()
        self.__load_service_handlers()

    def get_new_region_session(self, region_name: str):
        return connect_aws_session(region_name=region_name, **self.aws_connect_key_dict)

    # ServiceHandlerInterface 를 상속받는 모든 하위 클래스 목록을 얻습니다
    def __load_service_handlers(self) -> None:
        """ServiceHandlerInterface 를 상속받는 모든 하위 클래스 목록을 얻습니다"""
        service_classes = self.inheritors(ServiceHandlerInterface)
        # print(f"service_handlers:{service_handlers}")
        for service_class in service_classes:
            self.service_dict[service_class.get_service_name()] = service_class(self.session, self.shared_dict, self.aws_account_id, self.aws_connect_key_dict)

    # 'klass' 클래스를 상속받는 모든 하위 클래스 목록(subclasses)을 얻습니다
    def inheritors(self, klass: ServiceHandlerInterface) -> set:
        """'klass' 클래스를 상속받는 모든 하위 클래스 목록(subclasses)을 얻습니다"""
        subclasses = set()
        work = [klass]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return subclasses

    def get_region_name(self, is_name_short: bool = True, is_language_eng: bool = True):
        return aws_region_to_str(self.region_name, is_name_short=is_name_short, is_language_eng=is_language_eng)
