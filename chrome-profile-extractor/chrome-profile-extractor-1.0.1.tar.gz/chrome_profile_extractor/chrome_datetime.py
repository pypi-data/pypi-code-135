from datetime import datetime, timedelta


# def get_chrome_datetime(chrome_date):
#     """Return a `datetime.datetime` object from a chrome format datetime
#     Since `chrome_date` is formatted as the number of microseconds since January 1601"""
#     return datetime(1601, 1, 1) + timedelta(microseconds=chrome_date)

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    if chromedate != 86400000000 and chromedate:
        try:
            return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
        except Exception as e:
            print(f"Error: {e}, chromedate: {chromedate}")
            return chromedate
    else:
        return ""
