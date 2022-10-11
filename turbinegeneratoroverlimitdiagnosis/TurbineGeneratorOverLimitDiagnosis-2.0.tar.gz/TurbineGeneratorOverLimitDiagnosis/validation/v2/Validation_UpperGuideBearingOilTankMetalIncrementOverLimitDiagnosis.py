from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis import UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis import UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]实测值(800.05)超限报警,阈值800.00', 'dfem_code': 'SP000480'}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]实测值(800.14)超限报警,阈值800.00', 'dfem_code': 'SP000480'}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]实测值(800.09)超限报警,阈值800.00', 'dfem_code': 'SP000480'}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]实测值(800.09)超限报警,阈值800.00', 'dfem_code': 'SP000480'}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]实测值(800.00)超限报警,阈值800.00', 'dfem_code': 'SP000480'}
        {'dfem_evidence': '[上导轴承油槽金属颗粒数量增加量]正常', 'dfem_code': ''}
    """
    np.random.seed(1234)
    tempers = (np.random.randn(10, 1)*0.1 + 800).flatten().tolist()

    obj = UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis()
    for i in tempers:
        print(
            obj.diagnosis(i)
        )


if __name__ == '__main__':
    main()