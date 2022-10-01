# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import geodesic.tesseract.models.inference_pb2 as inference__pb2


class InferenceServiceV1Stub(object):
    """InferenceService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendAssetData = channel.stream_stream(
                '/workerv1.InferenceServiceV1/SendAssetData',
                request_serializer=inference__pb2.SendAssetDataRequest.SerializeToString,
                response_deserializer=inference__pb2.SendAssetDataResponse.FromString,
                )
        self.GetModelInfo = channel.unary_unary(
                '/workerv1.InferenceServiceV1/GetModelInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=inference__pb2.ModelInfo.FromString,
                )


class InferenceServiceV1Servicer(object):
    """InferenceService
    """

    def SendAssetData(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModelInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InferenceServiceV1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendAssetData': grpc.stream_stream_rpc_method_handler(
                    servicer.SendAssetData,
                    request_deserializer=inference__pb2.SendAssetDataRequest.FromString,
                    response_serializer=inference__pb2.SendAssetDataResponse.SerializeToString,
            ),
            'GetModelInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModelInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=inference__pb2.ModelInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'workerv1.InferenceServiceV1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InferenceServiceV1(object):
    """InferenceService
    """

    @staticmethod
    def SendAssetData(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/workerv1.InferenceServiceV1/SendAssetData',
            inference__pb2.SendAssetDataRequest.SerializeToString,
            inference__pb2.SendAssetDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetModelInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/workerv1.InferenceServiceV1/GetModelInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            inference__pb2.ModelInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
