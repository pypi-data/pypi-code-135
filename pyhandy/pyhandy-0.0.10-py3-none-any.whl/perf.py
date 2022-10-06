'''
File:          perf.py
File Created:  2022-10-05 23:56:35
Author:        callmexss (callmexss@126.com)
Description:   handy perf tools.
'''
import time


class TimeHandy:
    """Time handy."""

    @staticmethod
    def get_format_time(epoch_time, fmt="%Y-%m-%d %H:%M:%S"):
        """Convert Epoch time to string format time.
        
        Arguments:
            epoch_time (float) -- epoch time
        
        Keyword Arguments:
            fmt (str) -- string format pattern (default: "%Y-%m-%d %H:%M:%S")

            Commonly used format codes:

            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.

        Returns:
            str -- string format time
        """
        return time.strftime(fmt, time.localtime(epoch_time))

    @staticmethod
    def get_epoch_time(date_time, pattern="%Y-%m-%d %H:%M:%S"):
        """Get epoch time from string format time.
        
        Arguments:
            date_time (str) -- string format time
        
        Keyword Arguments:
            pattern (str) -- string format pattern (default: "%Y-%m-%d %H:%M:%S")

            Commonly used format codes:

            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.
        
        Returns:
            float -- epoch time
        """
        return time.mktime(time.strptime(date_time, pattern))
