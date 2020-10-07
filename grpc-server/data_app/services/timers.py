from datetime import datetime, timedelta
from time import time
from google.protobuf import timestamp_pb2, duration_pb2
import pandas as pd


def datetimeFromISOString(datetime_str):
    """RFC3339"""
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')


def to_posix_timestamp(dt):
    return str((dt - datetime(1970, 1, 1)).total_seconds())


def timestamp_proto_from_datetime(dt):
    dt_ts_pb = timestamp_pb2.Timestamp()
    dt_ts_pb.FromDatetime(dt)
    return dt_ts_pb


def timestamp_proto_from_seconds(epoch_secs):
    return timestamp_pb2.Timestamp(seconds=epoch_secs)


def duration_proto_from_seconds(seconds):
    return duration_pb2.Duration(seconds=seconds)


def get_range(start, limit, tick):
    return pd.date_range(start, freq=tick, periods=limit)


def get_end(start, limit, tick):
    return start + tick*(limit-1)


if __name__ == "__main__":
    print(timestamp_pb2.Timestamp(seconds=int(time())))
    print(time())
    start = datetime.fromisoformat("2019-01-31 22:15:00")
    print(get_end(start, 3, timedelta(minutes=15)))
    print(get_range(start, 3, "15min").tolist())
