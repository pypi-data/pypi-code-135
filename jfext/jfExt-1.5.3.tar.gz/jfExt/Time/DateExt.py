# -*- coding: utf-8 -*-
"""
jf-ext.Time.DateExt.py
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018-2022 by the Ji Fu, see AUTHORS for more details.
:license: MIT, see LICENSE for more details.
"""

import time
import datetime


DISPLAY_DATE_FORMAT = "%Y年%m月%d日"
DISPLAY_TIME_FORMAT = "%Y年%m月%d日 %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def date_date_to_date_display_string(date):
    """
    >>> 日期转换成显示日期String
    :param {Date} date:
    :return {String}: 日期的String格式(日期)
    """
    return date.strftime(DISPLAY_DATE_FORMAT)


def date_date_to_time_display_string(date):
    """
    >>> 日期转换成显示时间String
    :param {Date} date:
    :return {String}: 日期的String格式(时间)
    """
    return date.strftime(DISPLAY_TIME_FORMAT)


def date_date_to_date_string(date):
    """
    >>> 日期转换成日期String
    :param {Date} date:
    :return {String}: 日期的String格式(日期)
    """
    return date.strftime(DATE_FORMAT)


def date_date_to_time_string(date):
    """
    >>> 日期转换成时间String
    :param {Date} date:
    :return {String}: 日期的String格式(时间)
    """
    return date.strftime(TIME_FORMAT)


def date_now_date():
    """
    >>> 获取当前时间的日期
    :return {date}: the date of now
    """
    now = datetime.datetime.now()
    return now


def date_today_date():
    """
    >>> 获取当天的日期
    :return {date}: the date of today
    """
    today = datetime.date.today()
    return today


def date_today_date_String():
    """
    >>> 获取当天的日期 String
    :return {String}: the date of today (String)
    """
    today = datetime.date.today()
    todayDateStr = today.strftime(DATE_FORMAT)
    return todayDateStr


def date_diff_from_date(date1, date2):
    """
    >>> 获取日期1 与 日期2 相差天数
    :param {String} date1: 2021-09-10
    :param {String} date2: 2021-09-10
    :return {Int}: the diff days of date1 and date2
    """
    first_date = datetime.datetime.strptime(date1, DATE_FORMAT)
    second_date = datetime.datetime.strptime(date2, DATE_FORMAT)
    return (first_date - second_date).days


def date_weeks_of_year_by_string(date_string):
    """
    >>> 获取日期所在第几周
    :param {String} date_string: 日期
    :return {Int}: 第几周
    """
    date_time = time.strptime(date_string, DATE_FORMAT)
    weeks = time.strftime("%W", date_time)
    return weeks


def date_year_and_weeks_of_year_by_string(date_string):
    """
    >>> 获取日期所在第几周, 与 年份
    :param {String} date_string: 日期
    :return {[Int, Int]}: [年份, 第几周]
    """
    date_time = time.strptime(date_string, DATE_FORMAT)
    weeks = int(time.strftime("%W", date_time))
    year = int(time.strftime("%Y", date_time))
    if weeks < 1:
        weeks += 52
        year -= 1
    return [year, weeks]


def date_start_day_of_weeks(year, weeks):
    """
    >>> 获取一年指定周的周一时间
    :return {Date}:
    """
    # 当年第一天
    year_start_string = "{}-01-01".format(year)
    # 格式化为日期格式
    year_start = datetime.datetime.strptime(year_start_string, '%Y-%m-%d')
    # 当年第一天的周信息
    year_start_calendarmsg = year_start.isocalendar()
    # year_start_week = year_start_calendarmsg[1]
    year_start_weekday = year_start_calendarmsg[2]
    year_start_year = year_start_calendarmsg[0]
    if year_start_year < int(year):
        day_delat = (8 - int(year_start_weekday)) + (int(weeks) - 1) * 7
    else:
        day_delat = (8 - int(year_start_weekday)) + (int(weeks) - 2) * 7
    res = (year_start + datetime.timedelta(days=day_delat)).date()
    return res.strftime(DATE_FORMAT)


def date_time_before_today(days):
    """
    >>> 获取 days 天前时间
    :Returns {String}: the time of  n day before today
    """
    # 先获得时间数组格式的日期
    dateDayAgo = (datetime.datetime.now() - datetime.timedelta(days=days))
    # 转换为其他字符串格式
    otherStyleTime = dateDayAgo.strftime(DATE_FORMAT)
    return otherStyleTime


def date_time_after_today(days):
    """
    >>> 获取 days 天后时间
    :Returns {String}: the time of  n day before today
    """
    # 先获得时间数组格式的日期
    dateDayafter = (datetime.datetime.now() + datetime.timedelta(days=days))
    # 转换为其他字符串格式
    otherStyleTime = dateDayafter.strftime(DATE_FORMAT)
    return otherStyleTime


def date_time_before_date(date, days):
    """
    >>> 获取 days 天前时间
    :param {Date} date:
    :Returns {String}: the time of  n day before today
    """
    # 先获得时间数组格式的日期
    dateDayAgo = (date - datetime.timedelta(days=days))
    # 转换为其他字符串格式
    otherStyleTime = dateDayAgo.strftime(DATE_FORMAT)
    return otherStyleTime


def date_time_after_date(date, days):
    """
    >>> 获取 days 天后时间
    :param {Date} date:
    :Returns {String}: the time of  n day before today
    """
    # 先获得时间数组格式的日期
    dateDayafter = (date + datetime.timedelta(days=days))
    # 转换为其他字符串格式
    otherStyleTime = dateDayafter.strftime(DATE_FORMAT)
    return otherStyleTime


def date_yesterday_time():
    """
    >>> 获取昨天的时间
    :return {String}: the time of yesterday
    """
    oneday = datetime.timedelta(days=1)
    today = datetime.date.today()
    yesterday = today - oneday
    return yesterday


def date_this_monday():
    """
    >>> 获取本周周一日期
    :return: {String}: 返回周一的日期
    """
    # today = datetime.datetime.strptime(str(today), "%Y%m%d")
    today = datetime.date.today()
    return datetime.datetime.strftime(today - datetime.timedelta(today.weekday()), DATE_FORMAT)


def date_this_month_start():
    """
    >>> 获取本月一号
    :return {String}: 返回本月1号日期
    """
    now = datetime.date.today()
    this_month_start = datetime.datetime(now.year, now.month, 1)
    return datetime.datetime.strftime(this_month_start, DATE_FORMAT)


def date_today_time_range():
    """
    >>> 获取当天的时间起始与结束
    :return {[String, String]}: [start_time, end_time]
        [the start time, end time of today]
    """
    return date_time_range_by_date(date_today_date())


def date_yesterday_time_range():
    """
    >>> 获取昨日的时间起始与结束
    :return {[String, String]}: [start_time, end_time]
        [the start time of yesterday, end time of today of yesterday]
    """
    return date_time_range_by_date(date_yesterday_time())


def date_time_range_by_date(date):
    """
    >>> 获取时间起始与结束 by date
    :return {[String, String]}: [mintime, maxtime]
        [the start time, end time of date]
    """
    mintime = str(date) + ' ' + '00:00:00'
    maxtime = str(date) + ' ' + '23:59:59'
    return [mintime, maxtime]


def date_time_range_by_date_cin7(date):
    """
    >>> GMT标准时间 -> 新西兰时间 开始, 结束
    :param {String} date: 国际标准时间 (格式: %Y-%m-%d)
    :return {[String, String]}: [start_time, end_time]
    """
    oneday = datetime.timedelta(days=1)
    new_date = datetime.datetime.strptime(date, DATE_FORMAT)
    new_date_yesterday = new_date - oneday
    yesterday_date = new_date_yesterday.strftime(DATE_FORMAT)

    mintime = str(yesterday_date) + ' ' + '12:00:00'
    maxtime = str(date) + ' ' + '12:00:00'
    return [mintime, maxtime]


def date_string_validate(date_text):
    """
    >>> 时间字符串校验
    :param {String} date: (格式: %Y-%m-%d)
    return {Boolean}: 是否校验成功
    """
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False
