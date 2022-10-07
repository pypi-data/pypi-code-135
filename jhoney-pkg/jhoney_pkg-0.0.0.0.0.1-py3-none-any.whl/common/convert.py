import math
from si_prefix import si_format
from typing import List
import sys
import os


def convert_byte_size(byte_size: int, *, in_size_name="Bytes", out_size_name="Auto") -> str:
    """
    주어진 byte_size 값에 맞는 크기로 변환한 Str 값을 반환한다.
    - size_name에는 "Bytes", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"가 있다.
    - 이 단위는 각각 2^1, 2^10, 2^20, ..., 2^80 Byte 를 의미한다.
    - 해당 단위 소수점 2자리에서 반환한다.
    - in_size_name은 입력 byte_size 단위로, Default 값은 Bytes이다.
    - out_size_name은 출력 byte_size 단위로, Default 값은 Auto 이다.
        - Auto는 자동으로 "Bytes", "KiB", "MiB", "GiB", "TiB", ... 로 변환하는 것을 의미한다.
    """
    byte_size = float(byte_size)

    if byte_size == 0:
        if out_size_name == "Auto":
            out_size_name = "Bytes"
        return f"0 {out_size_name}"
    size_names_dict = {
        "B": 0,
        "Bytes": 0,
        "K": 1,
        "KiB": 1,
        "Kilobytes": 1,
        "M": 2,
        "MiB": 2,
        "Megabytes": 2,
        "G": 3,
        "GiB": 3,
        "Gigabytes": 3,
        "T": 4,
        "TiB": 4,
        "Terabytes": 4,
        "P": 5,
        "PiB": 5,
        "E": 6,
        "EiB": 6,
        "Z": 7,
        "ZiB": 7,
        "Y": 8,
        "YiB": 8,
    }
    size_names = ("Bytes", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    in_size_idx = size_names_dict.get(in_size_name, 0)
    out_size_idx = size_names_dict.get(out_size_name, 0)
    # print(f"in_size_idx : {in_size_idx}")
    # print(f"out_size_idx : {out_size_idx}")

    byte_size *= math.pow(1024, in_size_idx)
    # print(f"byte_size : {byte_size}")
    if out_size_name == "Auto":
        out_size_idx = int(math.floor(math.log(byte_size, 1024)))
    # print(f"out_size_idx : {out_size_idx}")
    p = math.pow(1024, out_size_idx)
    # print(f"p : {p}")
    byte_size /= p
    # print("byte_size:", byte_size)
    if byte_size == int(byte_size):
        s = int(byte_size)
    else:
        if out_size_name == "Auto":
            s = round(byte_size, 2)
        else:
            s = round(byte_size, 3)
    # print(f"s out_size_name : {s} {out_size_name}")
    out_size_name = size_names[out_size_idx]
    return f"{s} {out_size_name}"


def convert_number_to_si_size(number: float, precision: int = 1) -> str:
    """
    number 를 입력받아서, si 단위로 변환한다.
    - 미리 지원되는 si-prefix 라이브러리를 이용한다.
    - 문자열을 입력받으면 숫자로 변환후 처리한다.
    - precision 은 정밀도로, 소수점 몇 자리 까지 나타낼 것인지를 의미하며, Default 값은 1이다.
    - return 값 타입은 string이다.
    - 예시
        - number = .5 => 500.0 m (default precision is 1)
        - number = .01331 precision=2 => 13.31 13.31m
        - number = 1331 precision=2 => 1.33k
        - number = 1331 precision=0 => 1k
    """
    number = float(number)
    return si_format(number, precision=precision)


def convert_dict_datas_list_to_list_datas_list(dict_datas_list: List[dict], extract_key_dict: dict = {}, is_enclude_header=True) -> List[list]:
    """
    list[dict] 형태의 dict_datas_list 를 받아서, list[list] 형태의 list_datas_list 로 변환해서 반환한다.
    - 헤더를 첫번째 행에 넣고,
    - 나머지를 value 순으로 추출한다.
    - 이때 extract_key_dict 값을 통해서 원하는 키의 데이터만, 정의된 값의 순서대로, 또한 해더값도 지정된 값으로 부여할 수 있다.
    - 만약 dict_datas_list 이 빈 list라면, 첫 행은 extract_key_dict 의 key - value 값을, 두번째 행은 None 값을 넣는다.
    - is_enclude_header 의 Dafault 값은 True지만, 만약 False이면, 첫행은 포함시키지 않는다.
    """
    # 경우의 수는 총 4가지이다.
    # 1. dict_datas_list 가 있음
    #   1.1. extract_key_dict가 있음 -> 정상적으로 추출
    #   1.2. extract_key_dict가 없음 -> dict_datas_list [0]의 키값으로 모두 추출
    # 2. dict_datas_list 가 없음
    #   2.1. extract_key_dict가 있음 -> extract_key_dict의 키값만 헤더, value 값은 None
    #   2.2. extract_key_dict가 없음 -> 헤더, value 둘 다 None
    # + 여기서 is_enclude_header 여부에 따라 헤더를 포함시킬 수도, 배제할 수도 있다.

    list_datas_list = list()  # 채워넣고, 반환할 정보들 list[list]

    # 공통적으로 확인하는, extract_key_dict 값에 대해서 처리한다.
    header_keys = list()  # 추출할 객체의 추출할 실제 키값들(keys)
    header_vals = list()  # 추출할 객체에서, 변환할 헤더 값들 (values)
    if extract_key_dict:
        # 헤더는 대체할 val이 있으면 그 값으로, 없으면 기존 key값으로 결정한다.
        for key, val in extract_key_dict.items():
            if not val:
                val = key
            header_keys.append(key)
            header_vals.append(val)

    # 1. dict_datas_list 가 있음
    if dict_datas_list:
        # 1.1. extract_key_dict가 있음 -> 정상적으로 추출
        # 1.2. extract_key_dict가 없음 -> dict_datas_list [0]의 키값으로 모두 추출
        if not extract_key_dict:
            # extract_key_dict 값은 없지만, dict_datas_list 는 있으므로,
            # dict_datas_list  list 중 첫번째 dict 값의 key값으로 설정한다.
            # 이 경우의 header_keys, header_vals 는 동일한 값이다.
            header_keys = list(dict_datas_list[0].keys())
            header_vals = list(dict_datas_list[0].keys())

        # 이후, 헤더를 포함시킬지 여부에 따라 table_data 를 얻는다.
        cols = len(header_keys)  # 열
        rows = len(dict_datas_list)  # 행
        if is_enclude_header:
            rows += 1

        list_datas_list = [["" for _ in range(cols)] for _ in range(rows)]

        if is_enclude_header:
            for col, header in enumerate(header_vals):
                list_datas_list[0][col] = header

        for row, dict_data in enumerate(dict_datas_list):
            if is_enclude_header:
                row += 1
            for col, header in enumerate(header_keys):
                list_datas_list[row][col] = str(dict_data.get(header, " - "))

    # 2. dict_datas_list 가 없음 [거의 그럴일은 없겠지만...]
    else:
        # 2.1. extract_key_dict가 있음 -> extract_key_dict의 키값만 헤더, value 값은 None
        if extract_key_dict:
            # header_keys, header_vals는 앞서서 채워짐
            cols = len(header_keys)  # 열
            rows = 1  # 행
            if is_enclude_header:
                rows += 1

            list_datas_list = [["" for _ in range(cols)] for _ in range(rows)]

            for col, header in enumerate(header_vals):
                row = 0
                if is_enclude_header:
                    list_datas_list[0][col] = header
                    row += 1

                list_datas_list[row][col] = "None"

        # 2.2. extract_key_dict가 없음 -> 헤더, value 둘 다 None
        else:
            cols = 1  # 열
            rows = 1  # 행
            if is_enclude_header:
                rows += 1

            list_datas_list = [["" for _ in range(cols)] for _ in range(rows)]
            row = 0
            if is_enclude_header:
                list_datas_list[row][0] = "None"
                row += 1
            list_datas_list[row][0] = "None"

    return list_datas_list


def convert_dict_data_to_list_datas_list_vertical(dict_data: dict, extract_key_dict: dict = {}) -> List[list]:
    """
    단일 dictionary dict_data 받아서, list[list] 형태로 반환한다.
    - Key 값을 첫번째 열에 넣고, Value 값을 두번째 열에 넣는다.
    - 이때 extract_key_dict 값을 통해서 원하는 키의 데이터만, 정의된 값의 순서대로, 또한 해더값도 지정된 값으로 부여할 수 있다.
    """
    header_keys = list(dict_data.keys())
    header_vals = list(dict_data.keys())
    if extract_key_dict:
        header_keys = []
        header_vals = []
        for key, val in extract_key_dict.items():
            if not val:
                val = key
            header_keys.append(key)
            header_vals.append(val)

    rows = len(header_keys)  # 행
    cols = 2  # 열

    table_data = [["" for _ in range(cols)] for _ in range(rows)]
    for r, key in enumerate(header_keys):
        table_data[r][0] = header_vals[r]
        table_data[r][1] = str(dict_data.get(key, " - "))
    return table_data


def convert_file_ppt_to_pdf(input_file_name, output_file_name=None):
    """
    ppt 파일을 pdf 파일로 변환합니다.
    - input_file_name은 변환할 ppt 파일의 경로/이름입니다.
    - output_file_name은 변환된 pdf 파일의 경로/이름입니다.
        - output_file_name의 Default 값은 None이며, 이 경우, input_file_name과 동일한 경로에 동일한 이름의 pdf 파일이 생성됩니다.
        - output_file_name값이 별도로 지정된 경우, 별도로 지정된 경로의 지정된 이름의 pdf 파일이 생성됩니다.
    """
    if not input_file_name.lower().endswith((".ppt", ".pptx")):
        return

    from src.pkg_main_module import is_test_local_platform

    if not is_test_local_platform:
        return
    import comtypes.client

    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    print("input_file_name:", input_file_name)
    slides = powerpoint.Presentations.Open(input_file_name)

    if not output_file_name or not output_file_name.lower().endswith((".ppt", ".pptx")):
        output_file_name = input_file_name.replace(".ppt", ".pdf")
        output_file_name = input_file_name.replace(".pptx", ".pdf")

    slides.SaveAs(output_file_name, FileFormat=32)
    slides.Close()


# # main이면 실행합니다.
if __name__ == "__main__":
    # print("\n", convert_byte_size(0, "GiB"))
    # print("\n", convert_byte_size(1, in_size_name="GiB"))
    # print("\n", convert_byte_size(10, "GiB"))
    # print("\n", convert_byte_size(1, in_size_name="GiB"))
    # print("\n", convert_byte_size(1, in_size_name="GiB", out_size_name="M"))
    # print("\n", convert_byte_size(112000, out_size_name="GiB"))
    # print("\n", convert_byte_size(10000, "GiB"))
    # print("\n", convert_byte_size(100000, "GiB"))
    # print("\n", convert_byte_size(1000000, "GiB"))
    # print("\n", convert_byte_size(10000000, "GiB"))
    # print("\n", convert_byte_size(100000000, "GiB"))
    # print("\n", convert_byte_size(1000000000, "GiB"))
    # print("\n", convert_byte_size(10000000000, "GiB"))
    # print("\n", convert_byte_size(100000000000, "GiB"))
    # print("\n", convert_byte_size(1000000000000, "GiB"))
    # print("\n", convert_byte_size(10000000000000, "GiB"))
    # print("\n", convert_byte_size(100000000000000, "GiB"))
    pass
