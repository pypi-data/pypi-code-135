from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingOilViscosityHumidityOverLimitDiagnosis import UpperGuideBearingOilViscosityHumidityOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingOilViscosityOverLimitDiagnosis import UpperGuideBearingOilViscosityOverLimitDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽油黏度]实测值(43.58)超低限报警,阈值43.70', 'dfem_code': 'SP000460'}
        {'dfem_evidence': '[上导轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽油黏度]实测值(43.67)超低限报警,阈值43.70', 'dfem_code': 'SP000460'}
        {'dfem_evidence': '[上导轴承油槽油黏度]实测值(43.63)超低限报警,阈值43.70', 'dfem_code': 'SP000460'}
        {'dfem_evidence': '[上导轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽油黏度]实测值(43.64)超低限报警,阈值43.70', 'dfem_code': 'SP000460'}
        {'dfem_evidence': '[上导轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽油黏度]实测值(43.48)超低限报警,阈值43.70', 'dfem_code': 'SP000460'}
    """


    np.random.seed(1234)
    tempers = (np.random.randn(10, 1) * 0.1 + 43.7).flatten().tolist()

    obj = UpperGuideBearingOilViscosityOverLimitDiagnosis()
    for i in tempers:
        print(
            obj.diagnosis(i)
        )


if __name__ == '__main__':
    main()