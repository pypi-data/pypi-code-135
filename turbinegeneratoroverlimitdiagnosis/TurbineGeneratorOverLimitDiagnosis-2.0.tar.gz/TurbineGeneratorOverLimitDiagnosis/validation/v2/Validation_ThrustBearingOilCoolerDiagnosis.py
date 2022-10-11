from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingOilCoolerDiagnosis import ThrustBearingOilCoolerDiagnosis
# from tools.v2.Method_ThrustBearingOilCoolerDiagnosis import ThrustBearingOilCoolerDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(1.78),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(1.11),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(1.38),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(1.70),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(0.23),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(0.87),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(1.08),阈值0.10', 'dfem_code': 'SP000580'}
        {'dfem_evidence': '[推力轴承油冷却器]运行异常,冷油温度计算值偏差(0.99),阈值0.10', 'dfem_code': 'SP000580'}
    """
    np.random.seed(1234)
    tempers = (np.multiply(np.random.randn(10, 4), np.asarray([1, 1, 100, 1]).transpose()) + 80)
    obj = ThrustBearingOilCoolerDiagnosis()
    for item in tempers:
        print(obj.diagnosis(*item))


if __name__ == '__main__':
    main()
