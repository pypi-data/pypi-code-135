"""
    缓存服务 - mongo
    - 加载mysql中数据并缓存 - 方便查询 - 主要针对协议数据项
"""
from ats_base.base import req, api
from ats_base.config.configure import CONFIG
from ats_base.common.util import to_dict


def get(name: str, key: str):
    result = req.get('{}/{}/{}'.format(api.get(CONFIG.get('API', 'mm')), name, key))
    if result['code'] == 200:
        return result['data']

    raise Exception(result['message'])


def put(name: str, key: str, data):
    if type(data) is dict or type(data) is list:
        return req.post('{}/{}/{}'.format(api.get(CONFIG.get('API', 'mm')), name, key), jsons=data)
    else:
        return req.post('{}/{}/{}'.format(api.get(CONFIG.get('API', 'mm')), name, key), params=to_dict(data=data))


def delete(name: str, key: str):
    return req.delete('{}/{}/{}'.format(api.get(CONFIG.get('API', 'mm')), name, key))


def clear(name: str):
    return req.delete('{}/{}'.format(api.get('mm'), name))


def save_tester(hostname: str):
    return req.post('{}/{}/{}'.format(api.get(CONFIG.get('API', 'tester')), 'tester', hostname))


if __name__ == '__main__':
    METER_COMM = {
        "step_id": "*STEP_ID",
        "todo": {
            "meter:comm": {
                "msg": "#MESSAGE",
                "channel": '#CHANNEL',
                "frame": "#FRAME"
            }
        }
    }

    APP_Show = {
        "step_id": "*STEP_ID",
        "todo": {
            "app:show": {
                "msg": "#MESSAGE"
            }
        }
    }

    BENCH_POWER_OFF = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:power_off": {
                "msg": "#MESSAGE",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    BENCH_POWER_ON = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:power_on": {
                "msg": "#MESSAGE",
                "Phase": "#PHASE",
                "Rated_Volt": "#RATED_VOLTAGE",
                "Rated_Curr": "#RATED_CURRENT",
                "Rated_Freq": "#RATED_FREQUENT",
                "PhaseSequence": "#PH_SEQUENCE",
                "Revers": "#REVERS",
                "Volt_Per": "#VOLTAGE_PERCENT",
                "Curr_Per": "#CURRENT_PERCENT",
                "IABC": "#IABC",
                "CosP": "#COSP",
                "SModel": "#SMODEL",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    BENCH_ADJUST = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:adjust": {
                "msg": "#MESSAGE",
                "Phase": "#PHASE",
                "Rated_Volt": "#RATED_VOLTAGE",
                "Rated_Curr": "#RATED_CURRENT",
                "Rated_Freq": "#RATED_FREQUENT",
                "PhaseSequence": "#PH_SEQUENCE",
                "Revers": "#REVERS",
                "Volt_Per": "#VOLTAGE_PERCENT",
                "Curr_Per": "#CURRENT_PERCENT",
                "IABC": "#IABC",
                "CosP": "#COSP",
                "SModel": "#SMODEL",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    BENCH_ADJUST_CUST = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:adjust_cust": {
                "msg": "#MESSAGE",
                "Phase": "#PHASE",
                "Rated_Freq": "#RATED_FREQUENT",
                "Volt1": "#VOLTAGE1",
                "Volt2": "#VOLTAGE2",
                "Volt3": "#VOLTAGE3",
                "Curr1": "#CURRENT1",
                "Curr2": "#CURRENT2",
                "Curr3": "#CURRENT3",
                "Uab": "#UAB",
                "Uac": "#UAC",
                "Ang1": "#ANGLE1",
                "Ang2": "#ANGLE2",
                "Ang3": "#ANGLE3",
                "SModel": "#SMODEL",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    BENCH_ADJUST_UI2 = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:adjust_ui2": {
                "msg": "#MESSAGE",
                "Phase": "#PHASE",
                "Rated_Volt": "#RATED_VOLTAGE",
                "Rated_Curr": "#RATED_CURRENT",
                "Rated_Freq": "#RATED_FREQUENT",
                "PhaseSequence": "#PHASE_SEQUENCE",
                "Revers": "#REVERS",
                "Volt1_Per": "#VOLTAGE1_PERCENT",
                "Volt2_Per": "#VOLTAGE2_PERCENT",
                "Volt3_Per": "#VOLTAGE3_PERCENT",
                "Curr1_Per": "#CURRENT1_PERCENT",
                "Curr2_Per": "#CURRENT2_PERCENT",
                "Curr3_Per": "#CURRENT3_PERCENT",
                "IABC": "#IABC",
                "CosP": "#COSP",
                "SModel": "#SMODEL",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    BENCH_READ = {
        "step_id": "*STEP_ID",
        "todo": {
            "bench:read": {
                "msg": "#MESSAGE",
                "SModel": "#SMODEL",
                "Dev_Port": "#DEV_PORT"
            }
        }
    }

    put('app:manual', 'meter:comm', METER_COMM)
    put('app:manual', 'app:show', APP_Show)
    put('app:manual', 'bench:power_on', BENCH_POWER_ON)
    put('app:manual', 'bench:adjust', BENCH_ADJUST)
    put('app:manual', 'bench:adjust_cust', BENCH_ADJUST_CUST)
    put('app:manual', 'bench:adjust_ui2', BENCH_ADJUST_UI2)
    put('app:manual', 'bench:power_off', BENCH_POWER_OFF)
    put('app:manual', 'bench:read', BENCH_READ)
