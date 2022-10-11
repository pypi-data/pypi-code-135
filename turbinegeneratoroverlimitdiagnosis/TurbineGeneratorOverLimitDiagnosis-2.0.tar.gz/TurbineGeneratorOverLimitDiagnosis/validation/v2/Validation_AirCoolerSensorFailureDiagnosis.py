from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_AirCoolerSensorFailureDiagnosis import AirCoolerSensorFailureDiagnosis
# from tools.v2.Method_AirCoolerSensorFailureDiagnosis import AirCoolerSensorFailureDiagnosis

import numpy as np
import time, datetime


def main():
    """
    output:
        {'dfem_evidence': ['[空冷器温度]传感器峰峰值过小故障(0.00),阈值0.20$(group03)'], 'dfem_code': ['SP000412']}
        ……
        {'dfem_evidence': ['[空冷器温度]传感器峰峰值过小故障(0.00),阈值0.20$(group03)'], 'dfem_code': ['SP000412']}
        {'dfem_evidence': ['[空冷器温度]传感器温度超限故障(280.00),阈值205.00$(group01)'], 'dfem_code': ['SP000410']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        ……
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': '[空冷器温度]传感器温度超限故障(280.00),阈值205.00$(group01)', 'dfem_code': 'SP000410'}
        {'dfem_evidence': [], 'dfem_code': []}
        ……
        {'dfem_evidence': [], 'dfem_code': []}
        {'dfem_evidence': ['[空冷器温度]传感器极值点数量超限故障(5.00),阈值5.00$(group02)'], 'dfem_code': ['SP000411']}
        {'dfem_evidence': [], 'dfem_code': []}
    """


    extremeQuantOverLimit_values = [
        80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88,
        90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
        80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 280, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88,
        90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
        80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
    ]
    extremeQuantOverLimit_values = [80] * 24 + [280] + extremeQuantOverLimit_values
    extremeQuantOverLimit_times = np.add(time.time(),
                                         np.arange(len(extremeQuantOverLimit_values), 0, step=-1) * (-60)).tolist()

    obj = AirCoolerSensorFailureDiagnosis()
    for i in range(len(extremeQuantOverLimit_values)):
        print(
            obj.diagnosis(extremeQuantOverLimit_values[i], extremeQuantOverLimit_times[i])
        )


if __name__ == '__main__':
    main()