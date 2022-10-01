"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.streamswap.v1 import query_pb2 as osmosis_dot_streamswap_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sales = channel.unary_unary('/osmosis.streamswap.v1.Query/Sales', request_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySales.SerializeToString, response_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySalesResponse.FromString)
        self.Sale = channel.unary_unary('/osmosis.streamswap.v1.Query/Sale', request_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySale.SerializeToString, response_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySaleResponse.FromString)
        self.UserPosition = channel.unary_unary('/osmosis.streamswap.v1.Query/UserPosition', request_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPosition.SerializeToString, response_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPositionResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Sales(self, request, context):
        """Returns list of Sales ordered by the creation time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sale(self, request, context):
        """Returns the specific Sale object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Sales': grpc.unary_unary_rpc_method_handler(servicer.Sales, request_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySales.FromString, response_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySalesResponse.SerializeToString), 'Sale': grpc.unary_unary_rpc_method_handler(servicer.Sale, request_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySale.FromString, response_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySaleResponse.SerializeToString), 'UserPosition': grpc.unary_unary_rpc_method_handler(servicer.UserPosition, request_deserializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPosition.FromString, response_serializer=osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPositionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.streamswap.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Sales(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.streamswap.v1.Query/Sales', osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySales.SerializeToString, osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySalesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.streamswap.v1.Query/Sale', osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySale.SerializeToString, osmosis_dot_streamswap_dot_v1_dot_query__pb2.QuerySaleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.streamswap.v1.Query/UserPosition', osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPosition.SerializeToString, osmosis_dot_streamswap_dot_v1_dot_query__pb2.QueryUserPositionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)