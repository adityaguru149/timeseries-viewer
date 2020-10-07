import pytest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from data_app.autogen.meter_pb2_grpc import add_SearchServiceServicer_to_server

    return add_SearchServiceServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from data_app.server import Processor

    return Processor()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    from data_app.autogen.meter_pb2_grpc import SearchServiceStub

    return SearchServiceStub(grpc_channel)
