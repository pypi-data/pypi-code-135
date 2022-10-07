import datetime


def cur_time_str():
    now = datetime.datetime.now()
    return now.__str__()[0:19].replace(' ', '_').replace(':', '')
