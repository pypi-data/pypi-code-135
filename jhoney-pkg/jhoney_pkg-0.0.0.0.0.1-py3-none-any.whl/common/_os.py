import os
import yaml
import json

# 사실 이제는 불필요해진 함수인데, 그냥 냅둬본다.
def set_src_parent_abspath(file_abspath: str) -> str:
    """
    __file__ 값을 입력받고, 해당 모듈의 위치값으로부터 src를 찾고,
    src의 부모디렉토리 == 실행 프로그램 위치가 path 환경에 없으면 추가하고, 실행환경으로 지정합니다.
    """
    import sys, os

    # print(f"\n def set_src_parent_abspath(file_abspath={file_abspath})")

    # src의 절대경로를 찾는다.
    while file_abspath.split(os.sep)[-1] != "src":
        file_abspath = os.path.dirname(file_abspath)
        # print(file_abspath)

    # src의 부모 디렉토리를 path 환경에 추가 및 실행환경으로 지정한다.
    src_parent_abspath = os.path.dirname(file_abspath)
    # print(f"src_parent_abspath: {src_parent_abspath}")

    # src의 부모 디렉토리가 sys.path에 추가 되어있지 않으면 추가한다.
    if src_parent_abspath not in sys.path:
        sys.path.append(src_parent_abspath)
        os.chdir(src_parent_abspath)

    return src_parent_abspath


# 디렉토리를 새로 생성합니다.
def create_directory(directory: str) -> None:
    """
    디렉토리를 새로 생성합니다.
    - 'directory' 경로에 디렉토리가 없으면 디렉토리를 생성합니다.
    """
    from ._logging import logging

    try:
        # 해당 경로의 디렉토리가 이미 존재하면 무시한다.
        if not os.path.isdir(directory):
            os.makedirs(directory)
    except OSError:
        logging.critical_(f"Error: Creating directory '{directory}'")


# file_name 이름의 파일을 읽습니다(load 합니다).
def load_file_data(file_name: str, is_critical: bool = True) -> dict or list:
    """
    file_name 이름의 파일을 읽습니다(load 합니다).
    - 에러가 발생하면, logger에 exception_content을 저장하고, 빈 dict() 값을 반환합니다.
    """
    from ._logging import logging
    from .debug import get_exception_content

    loaded_file_data = dict()
    # file_name 이름의 파일이 존재하는지 확인
    if os.path.exists(file_name):
        try:  # 파일 읽기 예외처리
            with open(file_name, "r", encoding="utf-8") as ff:
                # 파일 읽고, yaml 파서로 데이터 Load하기
                loaded_file_data = yaml.load(ff, Loader=yaml.FullLoader)
        except Exception as e:  # 파일이 존재하는데 읽는데 실패한 케이스
            logging.critical_(get_exception_content(e))
    else:
        exception_content = f"'{file_name}' file does not exist.\n" ""
        if is_critical:
            logging.critical_(exception_content)
        else:
            logging.critical(exception_content)

    return loaded_file_data


def path_join(path, *paths) -> str:
    """os.path.join(path, *paths) 를 대신 수행해준다."""
    return os.path.join(path, *paths)


# file_name 이름의 파일에 input_data 를 저장합니다(save 합니다).
def save_file_data(file_name: str, input_data: dict or list, allow_unicode_: bool = False) -> None:
    """
    file_name 이름의 파일에 input_data 를 저장합니다(save 합니다).
      - file_name의 형식['.json' 또는 '.yaml']에 맞춰서 저장합니다.
      - allow_unicode_ 값이 True이면, 한글도 저장합니다.
      - 에러가 발생하면, logger에 exception_content을 저장합니다.
    """
    from ._logging import logging
    from .debug import get_exception_content

    try:  # 파일 읽기 예외처리
        file_format = file_name.split(".")[-1]

        with open(file_name, "w", encoding="utf-8") as ff:  # 혹시몰라서, 아스키코드로만 저장하는 코드 남겨둠
            if file_format == "json":
                ff.write(json.dumps(input_data, indent=4, ensure_ascii=(not allow_unicode_)))
            elif file_format == "yaml":
                ff.write(yaml.dump(input_data, allow_unicode=allow_unicode_))
    except Exception as e:  # 없으면 강제종료
        logging.critical_(get_exception_content(e))


def next_path(path_pattern: str) -> str:
    """
    Finds the next free path in an sequentially named list of files

    e.g. path_pattern = 'file-%s.txt':

    file-1.txt
    file-2.txt
    file-3.txt

    Runs in log(n) time where n is the number of existing files in sequence
    """
    i = 1

    # First do an exponential search
    while os.path.exists(path_pattern % i):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2  # interval midpoint
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)

    return path_pattern % b


if __name__ == "__main__":
    # _os.py functions test code
    os.chdir(os.path.dirname(__file__))

    # create_directory("12")
    # path_pattern = "file (%s).txt"
    # print(next_path(path_pattern))
