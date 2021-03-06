# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import meter_pb2 as meter__pb2


class SearchServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/data_app.SearchService/Search',
                request_serializer=meter__pb2.SearchRequest.SerializeToString,
                response_deserializer=meter__pb2.SearchResponse.FromString,
                )


class SearchServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=meter__pb2.SearchRequest.FromString,
                    response_serializer=meter__pb2.SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_app.SearchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SearchService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_app.SearchService/Search',
            meter__pb2.SearchRequest.SerializeToString,
            meter__pb2.SearchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
