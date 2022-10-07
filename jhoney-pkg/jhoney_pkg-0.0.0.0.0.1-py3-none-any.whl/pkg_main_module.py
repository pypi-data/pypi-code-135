import os, sys

# 작성자: J-Honey

# ※ 모듈의 전역변수 접근 시 주의점
# - 모듈의 전역변수는 모듈이 처음 세팅될 때의 값으로 공유된다.
# - 만약 모듈의 전역변수 값이 바뀌어도, 다른 모듈에서 가져다 쓰고 있는 전역변수 값은 바뀌지 않는다.
# - 그러므로 모듈의 전역변수 값 자체는 직접 접근을 해도 의미가 크게 없는 경우가 많다.
#
# 1. 한번 고정된 다음에 거의 변경될 여지가 없는 값는 직접 접근을 허용하고, 사용한다.
# 2. 한번 고정된 다음에 거의 변경될 여지가 있는 값는 직접 접근을 막고(__g_), Get, Set 함수로 접근한다.

# 현재 파일의 절대 경로의 부모 디렉토리의 부모디렉토리를 path 환경에 추가 및 실행환경으로 지정한다.
# 프로그램실행디렉토리\src\pkg_default_module.py
# => d:\03_업무수행\20210520_고객사AWS구축결과서_PPT_파이썬_자동생성\Create_AWS_Construction_Results
# 하지만... 여러가지 삽질 결과
# if __name__ == "__main__": 을 사용하면 해당 파일의 위치가 루트디렉토리가 되며,
# 해당 파일의 위치는 자동으로 sys.path에 추가한다는 것을 발견했다.

# 또한 테스트용 main 함수로 if __name__ == "__main__": 을 사용하지 않기로 해서
# sys.path.append(), os.chdir() 코드는 주석처리하겠다.
src_pkg_parent_abspath = os.path.dirname(os.path.dirname(__file__))
print(f"src_pkg_parent_abspath: {src_pkg_parent_abspath}")
# sys.path.append(src_pkg_parent_abspath)
# os.chdir(src_pkg_parent_abspath)
program_name = src_pkg_parent_abspath.split(os.sep)[-1]

from src import *
from datetime import datetime, date, timezone
import platform
import json
import sys

# print(len(sys.path), sys.path)

# 실행하는 플랫폼에 따라서, Windows 또는 WSL2 환경이면, local_platform에서 수행하는 테스트 환경이라고 간주한다.
# 추후 AWS AssumeRole권한 문제와 연관이 있다. - 실제 실행 환경은 Linux 환경일 수도 있다.
platform_ = platform.platform()
is_test_local_platform = platform_.startswith("Windows") or "WSL" in platform_

program_execution_datetime_now = datetime.now(timezone.utc)  # 현재 실행 시간
program_execution_date = program_execution_datetime_now.astimezone().strftime("%Y%m%d")
program_execution_date_ = program_execution_datetime_now.astimezone().strftime("%Y-%m-%d")
program_execution_time = program_execution_datetime_now.astimezone().strftime("%H:%M:%S")
program_execution_datetime = program_execution_datetime_now.astimezone().strftime("%Y%m%d_%H%M%S")

# json.JSONEncoder.default 변경 = Json 데이터의 직렬화 문제 해결하기
def datetime_handler(self, obj):
    if isinstance(obj, datetime):
        return "iso-datetime:" + obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    return str(obj)


json.JSONEncoder.default = datetime_handler


# main이면 실행합니다.
if __name__ == "__main__":
    print(__file__)
    startTime = datetime.now()
    print(f"# [StartTime] : {startTime.strftime('%Y-%m-%d %p.%I:%M:%S %z')}")

    endTime = datetime.now()
    print(f"# [EndTime] : {endTime.strftime('%Y-%m-%d %p.%I:%M:%S %z')}")

    diff = endTime - startTime
    # print(f"# [Finished in]  {seconds_to_eng_time(diff.seconds)}")
