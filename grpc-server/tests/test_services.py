import pytest
from time import time
from datetime import datetime, timedelta
from data_app.services.timers import (timestamp_proto_from_seconds,
                                      duration_proto_from_seconds,
                                      timestamp_proto_from_datetime,
                                      get_range)
from data_app.services.readers import csv_read, TimeseriesReader
from google.protobuf import timestamp_pb2, duration_pb2


@pytest.fixture
def df():
    return csv_read("meterusage.csv")


@pytest.fixture
def str_file():
    import io

    raw_csv = """time,meterusage
    2019-01-31 23:15:00,56
    2019-01-31 23:30:00,57
    2019-01-31 23:45:00,54.5"""
    file_pointer = io.StringIO(raw_csv)
    return file_pointer


def test_stringio_read(str_file):
    df = csv_read(str_file)
    assert len(df.index) == 3


def test_csv_file_read():
    df = csv_read("meterusage.csv")
    print(df.head(2))
    print(df.dtypes)
    print(df.count())
    print(df.tail(2))
    print(df[df.meterusage.isna()])
    assert len(df.index) == 2975


def test_timeseries_reader_indexing_15min_found():
    csv = "meterusage.csv"
    start = datetime.fromisoformat("2019-01-31 20:15:00")
    limit = 3
    precision = "15min"
    tf = TimeseriesReader(csv)
    sliced, message = tf.get_data(start, limit, precision)
    print(sliced)
    assert message == "Found all"
    assert len(sliced.index) == 3
    assert len(sliced.columns) == 1


def test_timeseries_reader_indexing_15min_found_some():
    csv = "meterusage.csv"
    start = datetime.fromisoformat("2019-01-31 23:30:00")
    limit = 5
    precision = "15min"
    tf = TimeseriesReader(csv)
    sliced, message = tf.get_data(start, limit, precision)
    print(sliced)
    assert message == "Found some"
    assert len(sliced.index) == 2
    assert len(sliced.columns) == 1


def test_timeseries_reader_indexing_15min_found_none():
    csv = "meterusage.csv"
    start = datetime.now()
    limit = 2
    precision = "15min"
    tf = TimeseriesReader(csv)
    sliced, message = tf.get_data(start, limit, precision)
    print(sliced)
    assert message == "Found none"
    assert len(sliced.index) == 0
    assert len(sliced.columns) == 1


def test_time_range():
    start = datetime.fromisoformat("2019-01-31 22:15:00")
    time_range = get_range(start, 3, "15min")
    assert len(time_range) == 3


def test_timestamp_proto_from_datetime():
    now_ts_pb = timestamp_pb2.Timestamp()
    now_ts_pb.GetCurrentTime()
    now = datetime.utcnow()
    now_dt_ts_pb = timestamp_pb2.Timestamp()
    now_dt_ts_pb.FromDatetime(now)
    now_dt_ts_pb = timestamp_proto_from_datetime(now)
    print(now_ts_pb, now_dt_ts_pb)
    assert now_dt_ts_pb.seconds - now_ts_pb.seconds <= 1


def test_timestamp_proto_from_seconds():
    now = time()
    epoch_seconds = int(now)
    ts_pb = timestamp_proto_from_seconds(epoch_seconds)
    print(ts_pb)
    assert ts_pb.seconds == epoch_seconds


def test_duration_proto_from_seconds():
    hour = 60*60
    seconds = int(hour)
    ds_pb = duration_proto_from_seconds(seconds)
    print(ds_pb)
    assert ds_pb.seconds == seconds
