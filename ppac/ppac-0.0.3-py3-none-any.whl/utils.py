from datetime import datetime


def datetime_to_str(value):
    return value.isoformat()


def str_to_datetime(value):
    return datetime.fromisoformat(value)
