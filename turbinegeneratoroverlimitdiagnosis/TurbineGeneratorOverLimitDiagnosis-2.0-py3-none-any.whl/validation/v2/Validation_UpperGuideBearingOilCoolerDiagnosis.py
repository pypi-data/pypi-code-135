from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingOilCoolerDiagnosis import UpperGuideBearingOilCoolerDiagnosis
# from tools.v2.Method_UpperGuideBearingOilCoolerDiagnosis import UpperGuideBearingOilCoolerDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(1.80),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(1.09),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(1.40),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(1.70),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(0.23),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(0.88),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(1.08),阈值0.10', 'dfem_code': 'SP000490'}
        {'dfem_evidence': '[上导轴承油冷却器]运行异常,冷油温度计算值偏差(0.99),阈值0.10', 'dfem_code': 'SP000490'}
    """
    np.random.seed(1234)
    tempers = (np.multiply(np.random.randn(10, 4), np.asarray([1, 1, 100, 1]).transpose()) + 80)

    obj = UpperGuideBearingOilCoolerDiagnosis()
    for item in tempers:
        print(obj.diagnosis(*item))


if __name__ == '__main__':
    main()