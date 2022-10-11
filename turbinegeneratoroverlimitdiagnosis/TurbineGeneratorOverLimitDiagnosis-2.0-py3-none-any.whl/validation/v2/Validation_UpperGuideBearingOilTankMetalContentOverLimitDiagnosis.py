from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingOilTankMetalContentOverLimitDiagnosis import UpperGuideBearingOilTankMetalContentOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingOilTankMetalContentOverLimitDiagnosis import UpperGuideBearingOilTankMetalContentOverLimitDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(950.05)超限报警,阈值950.00', 'dfem_code': 'SP000470'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(950.14)超限报警,阈值950.00', 'dfem_code': 'SP000470'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(950.09)超限报警,阈值950.00', 'dfem_code': 'SP000470'}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(950.09)超限报警,阈值950.00', 'dfem_code': 'SP000470'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承油槽水分含量]实测值(950.00)超限报警,阈值950.00', 'dfem_code': 'SP000470'}
        {'dfem_evidence': '[上导轴承油槽水分含量]正常', 'dfem_code': ''}
    """


    np.random.seed(1234)
    tempers = (np.random.randn(10, 1) * 0.1 + 950).flatten().tolist()

    obj = UpperGuideBearingOilTankMetalContentOverLimitDiagnosis()
    for i in tempers:
        print(
            obj.diagnosis(i)
        )


if __name__ == '__main__':
    main()