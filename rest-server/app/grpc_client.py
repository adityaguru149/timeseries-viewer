import os
import grpc

from app.autogen import meter_pb2, meter_pb2_grpc
from google.protobuf import timestamp_pb2

grpc_uri = os.environ["GRPC_URI"]
channel = grpc.insecure_channel(grpc_uri)


def timestamp_proto_from_datetime(dt):
    dt_ts_pb = timestamp_pb2.Timestamp()
    dt_ts_pb.FromDatetime(dt)
    return dt_ts_pb


def timestamp_proto_to_datetime(ts_pb):
    return ts_pb.ToDatetime()


def search(start, limit, precision):
    start_pb2 = timestamp_proto_from_datetime(start)
    print(start_pb2, limit, precision)
    stub = meter_pb2_grpc.SearchServiceStub(channel)
    response = stub.Search(meter_pb2.SearchRequest(
        start=start_pb2, limit=limit, precision=precision))
    labels = list(map(timestamp_proto_to_datetime, response.time))
    data = list(map(float, response.usage))
    print(data)
    print({"labels": labels, "data": response.usage, "message": response.message})
    return {"labels": labels, "data": data, "message": response.message}
