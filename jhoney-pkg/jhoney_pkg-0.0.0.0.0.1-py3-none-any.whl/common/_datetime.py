"""
#### _datetime.py 모듈
- datetime 관련해서 보조해준다.
    - 좀 더 정확히는 Timezone을 명확하게 부여해서, 모두 어웨어 datetime 객체로 사용할 수 있도록 보조해준다.
"""
from datetime import datetime, timezone, timedelta

# 될 수 있으면, datetime의 timezone은 UTC이다.
def utc_now(tz=None):
    if tz is None or tz == "utc":
        tz = timezone.utc
    return datetime.now(tz)


# def change_tzinfo(dt):

# tzinfo: None (나이브 객체) -> tzinfo:KST (어웨어 객체)
def change_tzinfo(dt, tz=None):
    if tz == "utc":
        tz = timezone.utc
    return dt.astimezone(tz)


# 출력용 datetime의 timezone은 KST이다.
# tz 값이 None이면 자동으로 KST 값으로 출력된다.
def log_datetime_str(dt, tz=None):
    """
    #### log용 datetime string 을 반환한다.
    - tz 값이 None이면 자동으로 KST 값으로 출력된다.
    - UTC+00:00 으로 출력을 원하면, tz 값을 timezone.utc 값으로 입력해주면 된다.
    - 출력 형식: '%Y-%m-%d %p.%I:%M:%S %z'
      - 예시: 2022-03-03 PM.06:19:47 +0900
    """
    if tz == "utc":
        tz = timezone.utc
    return change_tzinfo(dt, tz).strftime("%Y-%m-%d %p.%I:%M:%S %z")


def dt_strftime(dt, tz=None, format="%Y-%m-%d %p.%I:%M"):
    if tz == "utc":
        tz = timezone.utc
    dt = change_tzinfo(dt, tz)
    str_ = dt.strftime(format)
    if format == "%Y-%m-%d %p.%I:%M":
        str_ += f" (UTC+9)"
        # timezone_ = change_tzinfo(dt, tz).strftime("%z")  # '+0900'
        # str_ += f" (UTC{timezone_[:3]})"
    return str_


# -------------------------------------------

# 초를 입력받아 읽기쉬운 한국 시간으로 변환합니다. (영어. Day, hour, minute, second)
def seconds_to_eng_time(in_seconds: int) -> str:
    """초를 입력받아 읽기쉬운 한국 시간으로 변환합니다. (영어. Day, hour, minute, second)"""
    t1 = timedelta(seconds=in_seconds)
    days = t1.days
    _sec = t1.seconds
    (hours, minutes, seconds) = str(timedelta(seconds=_sec)).split(":")
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    result = []
    if days >= 1:
        result.append(f"{days} Day")
    if hours >= 1:
        result.append(f"{hours} hour")
    if minutes >= 1:
        result.append(f"{minutes} minute")
    if seconds >= 0:
        result.append(f"{seconds} second")
    return " ".join(result)


def convert_relative_time(date, is_language_eng: bool = True):
    """
    Take a datetime and return its "age" as a string.
    The age can be in second, minute, hour, day, month or year. Only the
    biggest unit is considered, e.g. if it's 2 days and 3 hours, "2 days" will
    be returned.
    Make sure date is not in the future, or else it won't work.
    """

    def formatn(n, s, relative_time_str=""):
        """Add "s" if it's plural"""

        if n == 1:
            return f"1 {s} {relative_time_str}"
        elif n > 1:
            return f"{int(n)} {s} {relative_time_str}"

    def q_n_r(a, b):
        """Return quotient and remaining"""

        return a / b, a % b

    class PrettyDelta:
        def __init__(self, dt):
            now = datetime.now()
            dt = dt.replace(tzinfo=None)
            delta = now - dt
            self.day = delta.days
            self.second = delta.seconds
            # print(f"self.day : {self.day} / self.second : {self.second} ")

            relative_time_str = ""
            if self.second > 0:
                if is_language_eng:
                    relative_time_str = "ago"
                else:
                    relative_time_str = "전"
            else:
                if is_language_eng > 0:
                    relative_time_str = "after"
                else:
                    relative_time_str = "후"
                delta = dt - now
                self.day = delta.days
                self.second = delta.seconds

            self.relative_time_str = relative_time_str

            self.year, self.day = q_n_r(self.day, 365)
            # print(f"self.year : {self.year} / self.day : {self.day} ")
            self.month, self.day = q_n_r(self.day, 30.5)
            # print(f"self.month : {self.month} / self.day : {self.day} ")
            self.hour, self.second = q_n_r(self.second, 3600)
            # print(f"self.hour : {self.hour} / self.second : {self.second} ")
            self.minute, self.second = q_n_r(self.second, 60)
            # print(f"self.minute : {self.minute} / self.second : {self.second} ")

        def format(self, is_language_eng: bool = True):
            period_eng_kors = {"year": "년", "month": "개월", "day": "일", "hour": "시간", "minute": "분", "second": "초"}
            for period in period_eng_kors.keys():
                n = getattr(self, period)
                # print(f"period : {period} / n : {n} ")
                if n > 1:
                    if not is_language_eng:
                        period = period_eng_kors[period]
                    return formatn(n, period, self.relative_time_str)
            return "0 second" if is_language_eng else "0 초"

    pd = PrettyDelta(date)

    return pd.format(is_language_eng)


def test_main1():
    print(" ------------------- test_main ------------------- ")

    none_now = datetime.now()
    utc_now_ = utc_now()
    kst_now = change_tzinfo(utc_now_)

    print("---- nomal ----")
    print(f"none_now: {none_now} \t\t, log_datetime : {log_datetime_str(none_now)}")
    print(f"utc_now_ : {utc_now_}    \t, log_datetime : {log_datetime_str(utc_now_)}")
    print(f"kst_now : {kst_now}    \t, log_datetime : {log_datetime_str(kst_now)}")

    print("---- change_tzinfo ----")
    print("none_now")
    print(change_tzinfo(none_now))
    print(change_tzinfo(none_now, timezone.utc))
    print("utc_now_")
    print(change_tzinfo(utc_now_))
    print(change_tzinfo(utc_now_, timezone.utc))
    print("kst_now")
    print(change_tzinfo(kst_now))
    print(change_tzinfo(kst_now, timezone.utc))


def test_main2():
    # print(seconds_to_eng_time(0))
    # print(seconds_to_eng_time(1))
    # print(seconds_to_eng_time(10))
    # print(seconds_to_eng_time(100))
    # print(seconds_to_eng_time(1000))
    # print(seconds_to_eng_time(10000))
    # print(seconds_to_eng_time(100000))
    # print(seconds_to_eng_time(1000000))

    # print("\n", convert_relative_time(datetime(2021, 7, 18, 13, 26, 23)))
    # print("\n", datetime(2021, 11, 1, 16, 26, 23))
    print("\n", convert_relative_time(datetime.now(), False))
    print("\n", convert_relative_time(datetime(2021, 11, 1, 16, 26, 23)))
    print("\n", convert_relative_time(datetime(2021, 12, 1, 16, 26, 23)))


# main이면 실행합니다.
if __name__ == "__main__":
    startTime = utc_now()
    print(f"# [StartTime] : {log_datetime_str(startTime)}")

    test_main1()
    test_main2()

    endTime = utc_now()
    print(f"# [EndTime] : {log_datetime_str(endTime)}")
    # diff = endTime - startTime
    # print(f"# [Finished in]  {seconds_to_eng_time(diff.seconds)}")
