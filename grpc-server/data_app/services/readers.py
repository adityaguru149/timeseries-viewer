import logging
import pandas as pd
from datetime import datetime, timedelta
from data_app.services.timers import get_range


def csv_read(file_path, datetime_col="time"):
    return pd.read_csv(file_path, index_col=datetime_col, parse_dates=[datetime_col])


def get_using_index(df, time_range):
    try:
        sliced = df.loc[time_range]
        message = "Found all"
    except KeyError as e:
        logging.exception(e)
        message = "Found none"
        sliced = pd.DataFrame(data=[], index=[], columns=df.columns)
    return sliced, message


def slice_with_index(df, time_range):
    sliced = df.reindex(time_range)
    print(time_range)
    print(sliced)
    if sliced.meterusage.isna().any():
        sliced = sliced.dropna()
        if sliced.meterusage.any():
            message = "Found some"
        else:
            message = "Found none"
    else:
        message = "Found all"
    return sliced, message


class TimeseriesReader:
    def __init__(self, file, datetime_col="time"):
        self.df = csv_read(file, datetime_col=datetime_col)

    def get_data(self, start, limit, precision):
        time_range = get_range(start, limit, precision)
        # return get_using_index(self.df, time_range)
        return slice_with_index(self.df, time_range)
