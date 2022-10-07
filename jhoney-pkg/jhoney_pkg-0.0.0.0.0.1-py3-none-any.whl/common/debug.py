import json
import traceback
from functools import wraps


__g_stack_func = list()

# value_name의 value값을 출력하는 디버깅용 함수
def debuging_prt(value_name: str, value) -> None:
    """value_name의 value값을 출력하는 디버깅용 함수"""
    from ._logging import logging

    value_ = value
    if isinstance(value, dict):
        value_ = json.dumps(value, indent=4, ensure_ascii=False)

    logging.debug(f"[Debuging] {value_name}, type:{type(value)}, {value_!r}")


# functools.wrap - 데코레이터로 사용될 디버깅용 함수로, 함수가 시작될때&끝날때와 func_name 를 출력합니다.
def debuging_prt_func(func) -> None:
    """functools.wrap - 데코레이터로 사용될 디버깅용 함수로, 함수가 시작될 때 & 끝날 때, func_name 를 출력합니다."""
    from ._logging import logging

    global __g_stack_func

    # 시작할때 호출하는 함수
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if func_name not in __g_stack_func:
            __g_stack_func.append(func_name)
            logging.debug(f"[[B[ {len(__g_stack_func)}. func: {' => '.join(__g_stack_func[-2:])}()")
        result = func(*args, **kwargs)
        logging.debug(f"]]E] {len(__g_stack_func)}. func: {func_name}()\n")
        # logger.debug(f"call {func.__name__}({args!r}, {kwargs!r}) => return {result!r}\n")
        __g_stack_func.pop()
        return result

    return wrapper


# Exception 값을 받아서, Exception Name, Exception Content, traceback.format_exc을 조합한 exception_content값을 만들어서 반환합니다.
def get_exception_content(e: Exception) -> str:
    """Exception 값을 받아서, Exception Name, Exception Content, traceback.format_exc을 조합한 exception_content값을 만들어서 반환합니다."""
    exception_content = ""
    exception_content += f"Exception Name : {type(e).__name__}"
    exception_content += f"Exception Content : {str(e)}\n"
    exception_content += traceback.format_exc()
    return exception_content
