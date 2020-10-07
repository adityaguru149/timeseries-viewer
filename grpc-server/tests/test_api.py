from datetime import datetime, timedelta
from data_app.autogen import meter_pb2
from data_app.services import timers


def test_reply(grpc_stub):
    time_py = datetime.fromisoformat("2019-01-31 20:15:00")
    start = timers.timestamp_proto_from_datetime(time_py)
    limit = 2
    precision = "15min"
    print(start)
    request = meter_pb2.SearchRequest(
        start=start, limit=limit, precision=precision)
    response = grpc_stub.Search(request)

    print(response.time)
    assert response.message == "Found all"
    assert len(response.time) == len(response.usage)
    assert response.usage == [131.18, 129.98]
