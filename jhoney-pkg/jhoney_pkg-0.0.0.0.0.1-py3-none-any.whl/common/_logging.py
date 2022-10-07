# 프로그램의 로그 기록을 담당하는 모듈
import logging
import requests
import json
from os.path import join

from ..pkg_main_module import *
from ._os import create_directory

# 별도의 logging.Logger 함수를 생성하기 위한 클래스
class AddLogLevel(logging.Logger):
    """
    나만의 logging.Logger 함수를 생성하기 위한 클래스
    - 기존의 CRITICAL(50), ERROR(40) , WARNING(30), INFO(20), DEBUG(10) 의 5가지 log level 외에도
      DATA(15)와 TRACE(5) log level을 추가함

    - critical_ : critical log를 critical_logs, total_critical_logs에 별도로 각각 저장한다.
    - get_critical_logs : critical_logs[=list]를 반환한다. [ type_ ==1이면 critical_logs 을, 2면 total_critical_logs 을 작업한다.]
    - clear_critical_logs : critical_logs[=list]를 초기화한다. [total은 초기화할 수 없다]
    - isExist_critical_logs : critical_logs[=list]가 존재하는지 여부를 반환한다.
    - saveFile_critical_logs : 그동안 저장된 critical_logs의 내용을 로그 파일로 저장한다.
    - sendToSlack_critical_logs : critical_logs가 있으면 Slack으로 보낸다.
    """

    logging.addLevelName(logging.DEBUG + 5, "DATA")  # logging.DATA : 15 > logging.DEBUG: 10
    logging.addLevelName(logging.DEBUG - 5, "TRACE")  # logging.TRACE: 5 < logging.DEBUG: 10

    _critical_logs = list()
    _total_critical_logs = list()
    _log_level = logging.INFO
    _save_log_folder_name = join("Logs", "Default")

    # log_level 값을 반환한다.
    def get_log_level(self) -> int:
        """log_level 값을 반환한다."""
        return self._log_level

    # logging_level 값을 설정한다.
    def set_log_level(self, log_level: int) -> None:
        """logging_level 값을 설정한다."""
        self._log_level = log_level
        logger.setLevel(level=log_level)

    # save_log_folder_name 값 반환합니다.
    def get_save_log_folder_name(self) -> str:
        """save_log_folder_name 값을 반환한다."""
        return self._save_log_folder_name

    # save_log_folder_name 값을 변경하고, Logs에 새로운 디렉토리를 생성합니다.
    def set_save_log_folder_name(self, log_folder_name: str) -> None:
        """save_log_folder_name 값을 변경하고, Logs에 새로운 디렉토리를 생성합니다."""
        self._save_log_folder_name = join("Logs", log_folder_name)
        create_directory(self._save_log_folder_name)

        __g__file_handler = logging.FileHandler(join(self._save_log_folder_name, f"{program_execution_date}-logFile.txt"))
        # fileHandler = logging.FileHandler(f"{save_log_folder_name}/infoLevel-logFile.txt")
        logger.addHandler(__g__file_handler)

    def data(self, msg, *args, **kwargs) -> None:
        """
        #### logging.DATA == 15 인 로그를 저장한다.
        """
        self.log(logging.getLevelName("DATA"), msg, *args, **kwargs)

    def trace(self, msg, *args, **kwargs) -> None:
        """
        #### logging.TRACE == 5 인 로그를 저장한다.
        """
        self.log(logging.getLevelName("TRACE"), msg, *args, **kwargs)

    def critical_(self, msg, *args, **kwargs) -> None:
        """
        - log.critical()와 동일한 기능을 수행한다.
        - critical log를 critical_logs, total_critical_logs에 별도로 각각 저장한다.
        """
        self.log(logging.CRITICAL, msg, *args, **kwargs)
        self._critical_logs.append(msg)
        self._total_critical_logs.append(msg)

    def get_critical_logs(self, type_=1) -> list:
        """
        critical_logs[=list]를 반환한다.
        - type_ ==1이면 critical_logs 을, 2면 total_critical_logs 을 반환한다.
        """
        ret_val = self._critical_logs
        if type_ == 2:
            ret_val = self.total_critical_logs

        return ret_val

    def clear_critical_logs(self) -> None:
        """critical_logs[=list]를 초기화한다. [total은 초기화할 수 없다]"""
        self._critical_logs.clear()

    def isExist_critical_logs(self, type_=1) -> bool:
        """
        critical_logs[=list]가 존재하는지 여부를 반환한다.
        - type_ ==1이면 critical_logs 을, 2면 total_critical_logs 을 확인한다.
        """
        # 여담. 본래, list값이 존재하는지 여부는 list 그 자체만드로도 판별이 가능하다.
        # Ex. if self._critical_logs: ~~
        # 그러므로 초기 코드는 self._critical_logs 자체를 반환하는 것이었다.

        # 이는 결과적으로 옳게 돌아가지만 이는 내부의 불필요한 값을 유출시키는 것 같았고,
        # bool 값 그 자체만 반환하는 코드로 변경하였다.
        # 여기서도 return bool(self._critical_logs) 의 방식으로도 구현이 가능하지만,
        # 명확한 가독성을 위해서 len() 함수를 사용하겠다.

        ret_val = len(self._critical_logs) > 0
        if type_ == 2:
            ret_val = len(self.total_critical_logs) > 0

        return ret_val

    def saveFile_critical_logs(self, type_=1) -> None:
        """
        그동안 저장된 critical_logs의 내용을 로그 파일로 저장한다.
        - type_ ==1이면 critical_logs 을, 2면 total_critical_logs 을 저장한다.
        """
        critical_logs = self._critical_logs
        if type_ == 2:
            critical_logs = self.total_critical_logs

        if critical_logs:
            saveFile_name = f"{self._save_log_folder_name}/{program_execution_date}-critical_logs.txt"
            logger.info(f"Save '{saveFile_name}' file\n")
            with open(f"{saveFile_name}", "w") as ff:
                for critical_log in critical_logs:
                    ff.write(critical_log + "\n")
        else:
            logger.info("The file is not saved because the contents of the critical_logs are empty.\n")

    def sendToSlack_critical_logs(self, slack_urls: list = list(), type_=1) -> None:
        """
        critical_logs가 있으면 slack_urls 채널로 메시지를 보낸다.
        - type_ ==1이면 critical_logs 을, 2면 total_critical_logs 을 보낸다.
        """
        logs_name = "critical_logs"
        critical_logs = self._critical_logs
        if type_ == 2:
            logs_name = "total_critical_logs"
            critical_logs = self._total_critical_logs

        # logger.info(f"\n{logs_name}: {critical_logs}\n")

        if not critical_logs:
            return

        logger.info(f"※ {logs_name} exist. The content is transmitted to the Slack SA channel.\n")

        ### Step1. 슬랙으로 보낼 데이터 채우기
        fields = list()
        alarm_mean = f"본 알람이 왔다는 것은 {program_name} 프로그램에 치명적인 문제가 생겨서 중단되었다는 의미입니다.\n"
        alarm_mean += "문제가 문제인지 확인해야합니다."
        fields.append(
            {
                "title": f"경고! {program_name} 이 돌아가는 도중 문제가 발생했습니다.",
                "value": alarm_mean,
                "short": False,
            }
        )
        for i, critical_log in enumerate(critical_logs, 1):
            fields.append(
                {
                    "title": f"{i} 번째 critical_log\n",
                    "value": f"{critical_log}\n\n",
                    "short": False,
                }
            )

        payloads_title = f"[{program_execution_date_}]. {program_name} critical_logs - {len(critical_logs)} 개" ""
        payloads = {"attachments": [{"pretext": payloads_title, "color": "#0099A6", "fields": fields}]}

        ### Step2. 슬랙으로 데이터 보내기
        for slack_url in slack_urls:
            response = requests.post(
                slack_url,
                data=json.dumps(payloads),
                headers={"Content-Type": "application/json"},
            )

            if response.status_code != 200:
                raise ValueError(f"Request to slack returned an error {response.status_code}, the response is:\n{response.text}\n")

        # 데이터를 보냈으면 초기화하기
        if type_ == 1:
            self._critical_logs.clear()
        else:
            self._total_critical_logs.clear()


# print("test용 logger 전역공간 실행")

logger = None
logging.setLoggerClass(AddLogLevel)
logger = logging.getLogger("logger")
logger.setLevel(level=logger.get_log_level())  # 실제용


# Log 쌓을 디렉토리 생성
create_directory("Logs")
create_directory(logger.get_save_log_folder_name())

# log formatter :                  로깅레벨            |   메세지
__g_formatter = logging.Formatter("%(levelname)s    \t | %(message)s")

# handler 생성 (stream, file)
__g__stream_hander = logging.StreamHandler()
# __g__stream_hander.setFormatter(__g_formatter) # 그냥 터미널상의 출력은 제대로 출력
__g__file_handler = logging.FileHandler(join(logger.get_save_log_folder_name(), f"{program_execution_date}-logFile.txt"))
__g__file_handler.setFormatter(__g_formatter)  # log 파일만 로깅레벨을 추가해서 출력

# logger instance에 handler 설정
logger.addHandler(__g__stream_hander)
logger.addHandler(__g__file_handler)

# 모듈을 테스트 용으로 실행하는 함수
def module_test_run():
    """
    모듈을 테스트 용으로 실행하는 함수
    """
    print("my_logger.py - module_test_run()")

    print(f"__name__: {__name__}")  # ==> __name__: __main__
    # DEBUG, INFO, WARNING, ERROR, CRITICAL 의 5가지 등급이 기본적으로 사용된다.
    print(f"logging.CRITICAL : {logging.CRITICAL}")  # 50 # FATAL = CRITICAL
    print(f"logging.FATAL    : {logging.FATAL}")  # 50
    print(f"logging.ERROR    : {logging.ERROR}")  # 40
    print(f"logging.WARN     : {logging.WARN}")  # 30 # WARN = WARNING
    print(f"logging.WARNING  : {logging.WARNING}")  # 30
    print(f"logging.INFO     : {logging.INFO}")  # 20
    print(f"logging.DEBUG    : {logging.DEBUG}")  # 10
    print(f"logging.NOTSET   : {logging.NOTSET}")  #  0
    print(f"-----------------------------------")  #  0

    print("logging.getLevelName():", logging.getLevelName("TRACE"))

    print(f"_logger: {logger}")  # ==> _logger: <Logger my (INFO)>
    # _logger.setLevel(level=logging.DEBUG)
    print(logger.get_log_level())
    print(logger.set_log_level(1))
    print(logger.get_log_level())

    logger.critical("critical log")
    logger.critical_("save_critical log")
    logger.fatal("fatal log")
    logger.error("error log")
    logger.warning("warning log")
    logger.info("info log")
    logger.log(17, "17 level log")
    logger.data("data log")
    logger.debug("debug log")
    logger.trace("trace log")
