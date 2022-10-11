from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingOilTankHumidityOverLimitDiagnosis import UpperGuideBearingOilTankHumidityOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingOilTankHumidityOverLimitDiagnosis import UpperGuideBearingOilTankHumidityOverLimitDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(0.06)超限报警,阈值0.01', 'dfem_code': 'SP000450'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(0.16)超限报警,阈值0.01', 'dfem_code': 'SP000450'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(0.10)超限报警,阈值0.01', 'dfem_code': 'SP000450'}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(0.10)超限报警,阈值0.01', 'dfem_code': 'SP000450'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(0.02)超限报警,阈值0.01', 'dfem_code': 'SP000450'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
    """


    np.random.seed(1234)
    tempers = (np.random.randn(5, 1) * 0.1 + 0.015).flatten().tolist() + (
                np.random.randn(5, 1) * 0.1 + 0.015).flatten().tolist()

    obj = UpperGuideBearingOilTankHumidityOverLimitDiagnosis()
    for i in tempers:
        print(
            obj.diagnosis(i)
        )


if __name__ == '__main__':
    main()