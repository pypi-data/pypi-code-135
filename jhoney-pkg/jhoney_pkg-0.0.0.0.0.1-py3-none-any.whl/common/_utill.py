import uuid
import re
from operator import itemgetter, attrgetter


def dir_(obj) -> dict:
    """dir(obj)를 한 결과 중, __value__, _value, value로 분류해서 dict값으로 반환한다."""
    dirs = dir(obj)
    values = list()
    _values = list()
    __values__ = list()
    for _dir_ in dirs:
        if _dir_.startswith("__") and _dir_.endswith("__"):
            __values__.append(_dir_)
        elif _dir_.startswith("_"):
            _values.append(_dir_)
        else:
            values.append(_dir_)
    _dict = dict()
    if values:
        _dict["values"] = values
    # if _values:
    #     _dict["_values"] = _values
    # if __values__:
    #     _dict["__values__"] = __values__
    return _dict


# 입력받은 uuid_str 값이 uuid인지 검증합니다. 맞으면 True, 틀리면 False를 반환합니다.
def is_validate_uuid4(uuid_str: str) -> bool:
    """
    입력받은 uuid_str 값이 uuid인지 검증합니다.
    - 맞으면 True, 틀리면 False를 반환합니다.
    """
    is_validate = True
    try:
        uuid.UUID(uuid_str, version=4)
        # print("val:", val)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        is_validate = False

    return is_validate


def get_str_length(string: str, kor_len: int = 2, other_len: int = 1):
    """
    입력받은 문자열의 길이를 세서 반환한다.
    - 한글은 길이를 2로 간주하고, 나머지는 1로 간주한다.
    - kor_len, other_len으로 임의로 지정할 수 있다.
    - ※☆◆ 과 같은 특수문자는 고려하지 않음
    """
    str_length = 0
    p = re.compile("[가-힣]+")
    for s in string:
        if p.match(s):
            str_length += kor_len
        else:
            str_length += other_len

    return str_length


def sorted_dict_list(dict_list: list, sortkeys: list or tuple = [], *, reverse=False) -> list or None:
    """
    dict 형태 값이 들어간 list 를 sortkeys의 순서대로 정렬한다.
    - 정렬된 값을 반환한다.
    - reverse 값이 True이면, 통째로 역정렬된다.
    """
    # print(f"sorted(dict_list, key=itemgetter({str(sortkeys)[1:-1]}))")
    return eval(f"sorted(dict_list, key=itemgetter({str(sortkeys)[1:-1]}), reverse=reverse)")


def multisort(xs, specs):
    # print("specs:", specs)
    for spec in reversed(specs):
        if type(spec) == type("str"):
            key = spec
            reverse = False
        else:
            key = spec[0]
            if len(spec) >= 2:
                reverse = spec[1]
            else:
                reverse = False
        # print(f"key : {key}, reverse: {reverse}")
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs


def split_ip(ip: str):
    """
    Split a ip or cidr address given as string into a 4 ~ 5-tuple of integers.
    - If an incorrect value is entered for ip, it is sent to the back.
    - ex. ip: "10.205.132.128" => return :  [10, 205, 132, 128]
    - ex. ip: "10.205.132.128/26" => return :  [10, 205, 132, 128, 26]
    """
    if "." not in ip:
        return [255, 255, 255, 255, 255]
    split_ip = ip.split(".")
    last = split_ip[-1]
    split_ip.extend(last.split("/"))
    split_ip.remove(last)
    return list(int(ip) for ip in split_ip)


if __name__ == "__main__":
    print("_untill.py test main")
