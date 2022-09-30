import unittest

from .context import yfc_dat as yfcd
from .context import yfc_time as yfct

import pandas as pd
import numpy as np

from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo

from pprint import pprint

## 2022 calendar:
## X* = day X is USA public holiday that closed NYSE
##  -- February --
##  Mo   Tu   We   Th   Fr   Sa   Su
##  7    8    9    10   11   12   13
##  14   15   16   17   18   19   20
##  21*  22   23   24   25   26   27
##  28

class Test_Market_Intervals_USA(unittest.TestCase):

    def setUp(self):
        self.market = "us_market"
        self.exchange = "NMS"
        self.market_tz = ZoneInfo('America/New_York')
        self.market_open_time = time(9,30)
        self.market_close_time = time(16,0)


    def test_GetScheduleIntervals_hourly(self):
        interval = yfcd.Interval.Hours1

        for d in [14,15,16,17,18]:
            start_d = date(2022,2,d)
            end_d   = date(2022,2,d+1)

            response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_d, end_d, weeklyUseYahooDef=False)
            answer_times = [(time( 9,30), time(10,30)), 
                            (time(10,30), time(11,30)), 
                            (time(11,30), time(12,30)), 
                            (time(12,30), time(13,30)), 
                            (time(13,30), time(14,30)), 
                            (time(14,30), time(15,30)), 
                            (time(15,30), time(16,0))]
            left  = [datetime.combine(start_d, t1, self.market_tz) for t1,t2 in answer_times]
            right = [datetime.combine(start_d, t2, self.market_tz) for t1,t2 in answer_times]
            answer = pd.IntervalIndex.from_arrays(left, right, closed="left")
            try:
                self.assertTrue((response==answer).all())
            except:
                print("response:")
                pprint(response)
                print("answer:")
                pprint(answer)
                raise

            start_dt = datetime.combine(start_d, time(11,30), tzinfo=self.market_tz)
            end_dt   = datetime.combine(start_d, time(14,30), tzinfo=self.market_tz)
            response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_dt, end_dt, weeklyUseYahooDef=False)
            answer_times = [(time(11,30), time(12,30)),
                            (time(12,30), time(13,30)),
                            (time(13,30), time(14,30))]
            left  = [datetime.combine(start_d, t1, self.market_tz) for t1,t2 in answer_times]
            right = [datetime.combine(start_d, t2, self.market_tz) for t1,t2 in answer_times]
            answer = pd.IntervalIndex.from_arrays(left, right, closed="left")
            try:
                self.assertTrue((response==answer).all())
            except:
                print("response:")
                pprint(response)
                print("answer:")
                pprint(answer)
                raise

            start_dt = datetime.combine(start_d, time(11,0), tzinfo=self.market_tz)
            end_dt   = datetime.combine(start_d, time(14,0), tzinfo=self.market_tz)
            response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_dt, end_dt, weeklyUseYahooDef=False)
            answer_times = [(time(11,30), time(12,30)),
                            (time(12,30), time(13,30))]
            left  = [datetime.combine(start_d, t1, self.market_tz) for t1,t2 in answer_times]
            right = [datetime.combine(start_d, t2, self.market_tz) for t1,t2 in answer_times]
            answer = pd.IntervalIndex.from_arrays(left, right, closed="left")
            try:
                self.assertTrue((response==answer).all())
            except:
                print("response:")
                pprint(response)
                print("answer:")
                pprint(answer)
                raise

    def test_GetScheduleIntervals_dayWeek(self):
        interval = yfcd.Interval.Days1
        start_d = date(2022,2,14) # Monday
        end_d   = date(2022,2,26) # next Saturday
        response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_d, end_d, weeklyUseYahooDef=False)
        answer_days = [date(2022,2,14), date(2022,2,15), date(2022,2,16), date(2022,2,17), date(2022,2,18), 
                                        date(2022,2,22), date(2022,2,23), date(2022,2,24), date(2022,2,25)]
        answer_days = np.array(answer_days)
        answer = yfcd.DateIntervalIndex.from_arrays(answer_days, answer_days+timedelta(days=1), closed="left")
        try:
            self.assertTrue(response==answer)
        except:
            print("response:")
            pprint(response)
            print("answer:")
            pprint(answer)
            raise

        intervals = [yfcd.Interval.Days5, yfcd.Interval.Week]
        start_d = date(2022,2,14) # Monday
        end_d   = date(2022,2,26) # next Saturday
        answer = yfcd.DateIntervalIndex.from_arrays([date(2022,2,14),date(2022,2,22)], [date(2022,2,19),date(2022,2,26)], closed="left")
        for interval in intervals:
            response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_d, end_d, weeklyUseYahooDef=False)
            try:
                self.assertTrue(response==answer)
            except:
                print("response:")
                pprint(response)
                print("answer:")
                pprint(answer)
                raise
        # Start/end dates are in middle of week:
        start_d = date(2022,2,9) # Wednesday
        end_d   = date(2022,2,23) # Wednesday
        answer = yfcd.DateIntervalIndex.from_arrays([date(2022,2,14)], [date(2022,2,19)], closed="left")
        for interval in intervals:
            response = yfct.GetExchangeScheduleIntervals(self.exchange, interval, start_d, end_d, weeklyUseYahooDef=False)
            try:
                self.assertTrue(response==answer)
            except:
                print("response:")
                pprint(response)
                print("answer:")
                pprint(answer)
                raise


    def test_GetTimestampCurrentInterval_open(self):
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        for i in range(len(intervals)):
            interval = intervals[i]
            interval_td = yfcd.intervalToTimedelta[interval]
            for d in [14,15,16,17,18]:
                day = date(2022,2,d)
                for t in times:
                    ## dt at start of interval:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                    answer = {"interval_open":datetime.combine(day, t, self.market_tz), 
                             "interval_close":datetime.combine(day, t, self.market_tz)+interval_td}
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(day, self.market_close_time, self.market_tz)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

                    ## dt in middle of interval:
                    dt = datetime.combine(day, t, self.market_tz) + 0.5*interval_td
                    market_close_dt = datetime.combine(day, self.market_close_time, self.market_tz)
                    if dt >= market_close_dt:
                        dt = market_close_dt - timedelta(minutes=1)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                    answer = {"interval_open":datetime.combine(day, t, self.market_tz),
                             "interval_close":datetime.combine(day, t, self.market_tz)+interval_td}
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(day, self.market_close_time, self.market_tz)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        intervals = []
        intervals.append(yfcd.Interval.Days1)
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [14,15,16,17,18]:
                day = date(2022,2,d)
                for t in times:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                    if interval == yfcd.Interval.Days1:
                        answer = {"interval_open":day, "interval_close":day+timedelta(days=1)}
                    else:
                        answer = {"interval_open":date(2022,2,14), "interval_close":date(2022,2,19)}
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        ## weeklyUseYahooDef = False
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        day = date(2022,2,22) # Tuesday after public holiday
        times = []
        times.append(time(8))
        times.append(time(18))
        answer = {"interval_open":day, "interval_close":day+timedelta(days=4)}
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [22,23,24,25]:
                day = date(2022,2,d)
                for t in times:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval, weeklyUseYahooDef=False)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        ## weeklyUseYahooDef = True
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        day = date(2022,2,21) # Public holiday
        times = []
        times.append(time(8))
        times.append(time(18))
        answer = {"interval_open":day, "interval_close":day+timedelta(days=5)}
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [21,22,23,24,25]:
                day = date(2022,2,d)
                for t in times:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval, weeklyUseYahooDef=True)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

    def test_GetTimestampCurrentInterval_closed(self):
        answer = None

        ## Before/after market hours
        times = []
        times.append(time(9, 29))
        times.append(time(16, 0))
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [14,15,16,17,18]:
                day = date(2022,2,d)
                for t in times:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        ## Weekend, at times that would be open if weekday
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        intervals.append(yfcd.Interval.Days1)
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [19,20]:
                day = date(2022,2,d)
                for t in times:
                    dt = datetime.combine(day, t, self.market_tz)
                    intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        ## Public holiday, at times that would be open if weekday
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        intervals.append(yfcd.Interval.Days1)
        day = date(2022,2,21)
        for i in range(len(intervals)):
            interval = intervals[i]
            for t in times:
                dt = datetime.combine(day, t, self.market_tz)
                intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

        ## Handle week-intervals separately
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        t = time(10,0)
        ## 1) weeklyUseYahooDef=False
        for d in [19,20,21]:
            day = date(2022,2,d)
            dt = datetime.combine(day, t, self.market_tz)
            for i in range(len(intervals)):
                interval = intervals[i]
                intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval, weeklyUseYahooDef=False)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise
        ## 2) weeklyUseYahooDef=True, so self.monday_pubHol treated as in-interval
        for d in [19,20]:
            day = date(2022,2,d)
            dt = datetime.combine(day, t, self.market_tz)
            for i in range(len(intervals)):
                interval = intervals[i]
                intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, dt, interval, weeklyUseYahooDef=True)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

    def test_GetTimestampCurrentInterval_weeklyOnPubHoliday(self):
        intervals = [yfcd.Interval.Days5, yfcd.Interval.Week]
        day = date(2022,2,21)
        for interval in intervals:
            intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, day, interval, weeklyUseYahooDef=False)
            answer = None
            try:
                self.assertEqual(intervalRange, answer)
            except:
                print("interval = {0}".format(interval))
                print("d = {0}".format(d))
                print("intervalRange:")
                pprint(intervalRange)
                print("answer:")
                pprint(answer)
                raise

            intervalRange = yfct.GetTimestampCurrentInterval(self.exchange, day, interval, weeklyUseYahooDef=True)
            answer = {"interval_open":date(2022,2,21), "interval_close":date(2022,2,26)}
            try:
                self.assertEqual(intervalRange, answer)
            except:
                print("interval = {0}".format(interval))
                print("d = {0}".format(d))
                print("intervalRange:")
                pprint(intervalRange)
                print("answer:")
                pprint(answer)
                raise

    def test_GetTimestampCurrentInterval_hourly_batch(self):
        interval = yfcd.Interval.Hours1

        dts = []
        for d in range(7,21):
            dts.append(datetime(2022,2, d, 9,29,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d, 9,30,tzinfo=self.market_tz))
            for h in range(10,16):
                dts.append(datetime(2022,2, d, h,30,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d,16, 1,tzinfo=self.market_tz))

        responses = yfct.GetTimestampCurrentInterval_batch(self.exchange, dts, interval)
        for i in range(responses.shape[0]):
            response = responses.iloc[i]
            answer = yfct.GetTimestampCurrentInterval(self.exchange, dts[i], interval)
            if answer is None:
                try:
                    self.assertTrue(pd.isnull(response["interval_open"]))
                    self.assertTrue(pd.isnull(response["interval_close"]))
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise
            else:
                try:
                    self.assertEqual(response["interval_open"], answer["interval_open"])
                    self.assertEqual(response["interval_close"], answer["interval_close"])
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise

    def test_GetTimestampCurrentInterval_daily_batch(self):
        interval = yfcd.Interval.Days1

        dts = []
        for d in range(7,21):
            dts.append(datetime(2022,2, d, 9,29,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d, 9,30,tzinfo=self.market_tz))
            for h in range(10,16):
                dts.append(datetime(2022,2, d, h,30,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d,16, 1,tzinfo=self.market_tz))

        responses = yfct.GetTimestampCurrentInterval_batch(self.exchange, dts, interval)
        for i in range(responses.shape[0]):
            response = responses.iloc[i]
            answer = yfct.GetTimestampCurrentInterval(self.exchange, dts[i], interval)
            if answer is None:
                try:
                    self.assertTrue(pd.isnull(response["interval_open"]))
                    self.assertTrue(pd.isnull(response["interval_close"]))
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise
            else:
                try:
                    self.assertEqual(response["interval_open"], answer["interval_open"])
                    self.assertEqual(response["interval_close"], answer["interval_close"])
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise

    def test_GetTimestampCurrentInterval_weekly_batch(self):
        interval = yfcd.Interval.Week

        dts = []
        for d in range(7,21):
            dts.append(datetime(2022,2, d, 9,29,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d, 9,30,tzinfo=self.market_tz))
            for h in range(10,16):
                dts.append(datetime(2022,2, d, h,30,tzinfo=self.market_tz))
            dts.append(datetime(2022,2, d,16, 1,tzinfo=self.market_tz))

        # weeklyUseYahooDef=True
        responses = yfct.GetTimestampCurrentInterval_batch(self.exchange, dts, interval, weeklyUseYahooDef=True)
        for i in range(responses.shape[0]):
            response = responses.iloc[i]
            answer = yfct.GetTimestampCurrentInterval(self.exchange, dts[i], interval, weeklyUseYahooDef=True)
            if answer is None:
                try:
                    self.assertTrue(pd.isnull(response["interval_open"]))
                    self.assertTrue(pd.isnull(response["interval_close"]))
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise
            else:
                try:
                    self.assertEqual(response["interval_open"], answer["interval_open"])
                    self.assertEqual(response["interval_close"], answer["interval_close"])
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise

        # weeklyUseYahooDef=False
        responses = yfct.GetTimestampCurrentInterval_batch(self.exchange, dts, interval, weeklyUseYahooDef=False)
        for i in range(responses.shape[0]):
            response = responses.iloc[i]
            answer = yfct.GetTimestampCurrentInterval(self.exchange, dts[i], interval, weeklyUseYahooDef=False)
            if answer is None:
                try:
                    self.assertTrue(pd.isnull(response["interval_open"]))
                    self.assertTrue(pd.isnull(response["interval_close"]))
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise
            else:
                try:
                    self.assertEqual(response["interval_open"], answer["interval_open"])
                    self.assertEqual(response["interval_close"], answer["interval_close"])
                except:
                    print("Test fail with dt={}".format(dts[i]))
                    raise


    def test_GetTimestampNextInterval_open(self):
        ## If during day session, next interval is in same session:
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Hours1)
        times = []
        times.append(self.market_open_time)
        times.append(time(13, 30))
        for i in range(len(intervals)):
            interval = intervals[i]
            interval_td = yfcd.intervalToTimedelta[interval]
            # for weekday in range(5):
            for d in [14,15,16,17,18]:
                for t in times:
                    ## dt at start of interval:
                    dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                    intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
                    answer = {}
                    answer["interval_open"] = dt+interval_td
                    answer["interval_close"] = answer["interval_open"]+interval_td
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(answer["interval_close"].date(), self.market_close_time, self.market_tz)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

                    ## dt in middle of interval:
                    dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                    dt += interval_td * 0.5
                    market_close_dt = datetime.combine(dt.date(), self.market_close_time, self.market_tz)
                    if dt >= market_close_dt:
                        dt = market_close_dt - timedelta(minutes=1)
                    intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
                    answer = {}
                    answer["interval_open"] = datetime.combine(date(2022,2,d), t, self.market_tz) +interval_td
                    answer["interval_close"] = answer["interval_open"]+interval_td
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(answer["interval_close"].date(), self.market_close_time, self.market_tz)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise
        interval = yfcd.Interval.Mins90
        times = []
        answers = []
        times.append(time(9, 30))  ; answers.append({"interval_open":time(11, 0), "interval_close":time(12, 30)})
        times.append(time(9, 45))  ; answers.append({"interval_open":time(11, 0), "interval_close":time(12, 30)})
        times.append(time(13, 30)) ; answers.append({"interval_open":time(14, 0), "interval_close":time(15, 30)})
        times.append(time(13, 45)) ; answers.append({"interval_open":time(14, 0), "interval_close":time(15, 30)})
        for i in range(len(times)):
            t = times[i]
            answer_t = answers[i]
            for d in [14,15,16,17,18]:
                dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
                answer = {}
                answer["interval_open"]  = datetime.combine(date(2022,2,d), answer_t["interval_open"], self.market_tz)
                answer["interval_close"] = datetime.combine(date(2022,2,d), answer_t["interval_close"], self.market_tz)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

        # If during the final interval of session, next interval is next day first interval
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Hours1)
        intervals.append(yfcd.Interval.Mins90)
        for i in range(len(intervals)):
            interval = intervals[i]
            interval_td = yfcd.intervalToTimedelta[interval]

            times = []
            times.append(time(15, 59))
            m = min(15, interval_td.seconds//60//2)
            times.append(time(15, 59-m))
            for d in [14,15,16,17,18]:
                for t in times:
                    dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                    intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)

                    next_day = date(2022,2,d+1)
                    if next_day.weekday() in [5,6]:
                        next_day += timedelta(days=7-next_day.weekday())
                    while not yfct.ExchangeOpenOnDay(self.exchange, next_day):
                        next_day += timedelta(days=1)
                    answer = {}
                    answer["interval_open"] = datetime.combine(next_day, self.market_open_time, self.market_tz)
                    answer["interval_close"] = answer["interval_open"]+interval_td
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(answer["interval_close"].date(), self.market_close_time, self.market_tz)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        # If a day interval, is next working day regardless of today
        interval = yfcd.Interval.Days1
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        for d in [14,15,16,17,18]:
            for t in times:
                dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
                next_day = date(2022,2,d+1)
                if next_day.weekday() in [5,6]:
                    next_day += timedelta(days=7-next_day.weekday())
                while not yfct.ExchangeOpenOnDay(self.exchange, next_day):
                    next_day += timedelta(days=1)
                answer = {}
                answer["interval_open"] = next_day
                answer["interval_close"] = next_day+timedelta(days=1)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise
        dt = datetime.combine(date(2022,2,19), t, self.market_tz)
        intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
        answer = {}
        answer["interval_open"] = date(2022,2,22)
        answer["interval_close"] = date(2022,2,23)
        try:
            self.assertEqual(intervalRange, answer)
        except:
            print("interval = {0}".format(interval))
            print("dt = {0}".format(dt))
            print("intervalRange = {0}".format(intervalRange))
            print("answer = {0}".format(answer))
            raise

        ## weeklyUseYahooDef = False
        # If a week interval, is next working week regardless of today
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        # Next week
        answer = {}
        answer["interval_open"] = date(2022,2,22) # Skip Monday because holiday
        answer["interval_close"] = date(2022,2,26)
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [14,15,16,17,18,19]:
                for t in times:
                    dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                    intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval, weeklyUseYahooDef=False)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

        ## weeklyUseYahooDef = True
        # If a week interval, is next working week regardless of today
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        times = []
        times.append(self.market_open_time)
        times.append(time(15, 30))
        # Next week
        answer = {}
        answer["interval_open"] = date(2022,2,21) # Start on Monday despite holiday
        answer["interval_close"] = date(2022,2,26)
        for i in range(len(intervals)):
            interval = intervals[i]
            for d in [14,15,16,17,18,19]:
                for t in times:
                    dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                    intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval, weeklyUseYahooDef=True)
                    try:
                        self.assertEqual(intervalRange, answer)
                    except:
                        print("interval = {0}".format(interval))
                        print("dt = {0}".format(dt))
                        print("intervalRange:")
                        pprint(intervalRange)
                        print("answer:")
                        pprint(answer)
                        raise

    def test_GetTimestampNextInterval_closed(self):
        ## If in morning before market open, next interval next session first interval:
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        t = time(9,15)
        for i in range(len(intervals)):
            interval = intervals[i]
            interval_td = yfcd.intervalToTimedelta[interval]
            for d in [14,15,16,17,18]:
                dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)

                answer_day = date(2022,2,d)
                answer = {}
                answer["interval_open"]  = datetime.combine(answer_day, self.market_open_time, self.market_tz)
                if interval == yfcd.Interval.Days1:
                    answer["interval_close"] = datetime.combine(answer_day, self.market_close_time, self.market_tz)
                else:
                    answer["interval_close"] = answer["interval_open"]+interval_td
                    if answer["interval_close"].time() > self.market_close_time:
                        answer["interval_close"] = datetime.combine(answer["interval_close"].date(), self.market_close_time, self.market_tz)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

        ## If in afternoon after market close, next interval is next session first interval:
        intervals = []
        intervals.append(yfcd.Interval.Mins1)
        intervals.append(yfcd.Interval.Mins2)
        intervals.append(yfcd.Interval.Mins5)
        intervals.append(yfcd.Interval.Mins15)
        intervals.append(yfcd.Interval.Mins30)
        intervals.append(yfcd.Interval.Mins60)
        intervals.append(yfcd.Interval.Mins90)
        intervals.append(yfcd.Interval.Hours1)
        t = self.market_close_time
        for i in range(len(intervals)):
            interval = intervals[i]
            interval_td = yfcd.intervalToTimedelta[interval]
            for d in [14,15,16,17,18]:
                dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)

                next_day = date(2022,2,d+1)
                if next_day.weekday() in [5,6]:
                    next_day += timedelta(days=7-next_day.weekday())
                while not yfct.ExchangeOpenOnDay(self.exchange, next_day):
                    next_day += timedelta(days=1)
                answer = {}
                answer["interval_open"]  = datetime.combine(next_day, self.market_open_time, self.market_tz)
                answer["interval_close"] = answer["interval_open"]+interval_td
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

        # If day interval, is next working day regardless of today
        interval = yfcd.Interval.Days1
        times = []
        times.append(time(9, 0))
        times.append(time(16, 0))
        for d in [14,15,16,17,18]:
            for t in times:
                dt = datetime.combine(date(2022,2,d), t, self.market_tz)
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)

                next_day = date(2022,2,d+1)
                if next_day.weekday() in [5,6]:
                    next_day += timedelta(days=7-next_day.weekday())
                while not yfct.ExchangeOpenOnDay(self.exchange, next_day):
                    next_day += timedelta(days=1)
                answer = {}
                answer["interval_open"]  = next_day
                answer["interval_close"] = next_day+timedelta(days=1)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise

        # If a week interval, is next week regardless of today
        intervals = []
        intervals.append(yfcd.Interval.Days5)
        intervals.append(yfcd.Interval.Week)
        dates = []
        dates.append(datetime.combine(date(2022,2,18), time(16, 0), self.market_tz))
        dates.append(datetime.combine(date(2022,2,19), time(12, 0), self.market_tz))
        dates.append(datetime.combine(date(2022,2,20), time(12, 0), self.market_tz))
        for i in range(len(intervals)):
            interval = intervals[i]
            for dt in dates:
                intervalRange = yfct.GetTimestampNextInterval(self.exchange, dt, interval)
                answer = {}
                answer["interval_open"]  = date(2022,2,14+7)
                answer["interval_close"] = date(2022,2,14+7+5)
                try:
                    self.assertEqual(intervalRange, answer)
                except:
                    print("interval = {0}".format(interval))
                    print("dt = {0}".format(dt))
                    print("intervalRange:")
                    pprint(intervalRange)
                    print("answer:")
                    pprint(answer)
                    raise


if __name__ == '__main__':
    unittest.main()

    # # Run tests sequentially:
    # import inspect
    # test_src = inspect.getsource(Test_Market_Intervals_USA)
    # unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: (
    #     test_src.index(f"def {x}") - test_src.index(f"def {y}")
    # )
    # unittest.main(verbosity=2)
