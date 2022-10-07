# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class VpcHandler(ServiceHandlerInterface):
    # VPC는 고유한 vpc서비스를 가지고 있는 것이 아니라, ec2서비스를 이용하므로
    # default init 함수를 사용할 수가 없습니다.
    def client_setting(self):
        self.client = self.get_aws_client("ec2")

    @classmethod
    def get_service_name(cls):
        return "vpc"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_vpcs(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_vpcs, Filters=Filters)
        return response

    def describe_subnets(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_subnets, Filters=Filters)
        return response

    def describe_flow_logs(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_flow_logs, Filters=Filters)
        return response

    def describe_internet_gateways(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_internet_gateways, Filters=Filters)
        return response

    def describe_route_tables(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_route_tables, Filters=Filters)
        return response

    def describe_nat_gateways(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_nat_gateways, Filters=Filters)
        return response

    def describe_security_groups(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_security_groups, Filters=Filters)
        return response

    def describe_transit_gateways(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_transit_gateways, Filters=Filters)
        return response

    def describe_transit_gateway_route_tables(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_transit_gateway_route_tables, Filters=Filters)
        return response

    def describe_transit_gateway_attachments(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_transit_gateway_attachments, Filters=Filters)
        return response

    def search_transit_gateway_routes(self, TransitGatewayRouteTableId: str, Filters: list = []):
        response = Paginator.describe_allpages(self.client.search_transit_gateway_routes, Filters=Filters, TransitGatewayRouteTableId=TransitGatewayRouteTableId)
        return response

    def describe_vpc_endpoints(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_vpc_endpoints, Filters=Filters)
        return response

    def describe_vpc_endpoint_services(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_vpc_endpoint_services, Filters=Filters)
        return response

    def describe_addresses(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_addresses, Filters=Filters)
        return response

    def describe_network_interfaces(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_network_interfaces, Filters=Filters)
        return response

    def describe_vpn_gateways(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_vpn_gateways, Filters=Filters)
        return response

    def describe_vpn_connections(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_vpn_connections, Filters=Filters)
        return response

    def describe_customer_gateways(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_customer_gateways, Filters=Filters)
        return response
