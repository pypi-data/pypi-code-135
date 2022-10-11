from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingOilTankMetalContentOverLimitDiagnosis import ThrustBearingOilTankMetalContentOverLimitDiagnosis
# from tools.v2.Method_ThrustBearingOilTankMetalContentOverLimitDiagnosis import ThrustBearingOilTankMetalContentOverLimitDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承油槽水分含量]实测值(950.05)超限报警,阈值950.00', 'dfem_code': 'SP000560'}
        {'dfem_evidence': '[推力轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽水分含量]实测值(950.14)超限报警,阈值950.00', 'dfem_code': 'SP000560'}
        {'dfem_evidence': '[推力轴承油槽水分含量]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽水分含量]正常', 'dfem_code': ''}
    """
    np.random.seed(1234)
    tempers = (np.random.randn(5, 1) * 0.1 + 950).flatten().tolist()
    obj = ThrustBearingOilTankMetalContentOverLimitDiagnosis()
    for i in tempers:
        print(obj.diagnosis(i))


if __name__ == '__main__':
    main()
