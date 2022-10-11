from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingOilViscosityOverLimitDiagnosis import ThrustBearingOilViscosityOverLimitDiagnosis
# from tools.v2.Method_ThrustBearingOilViscosityOverLimitDiagnosis import ThrustBearingOilViscosityOverLimitDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承油槽油黏度]实测值(43.75)超低限报警,阈值43.70', 'dfem_code': 'SP000550'}
        {'dfem_evidence': '[推力轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽油黏度]实测值(43.84)超低限报警,阈值43.70', 'dfem_code': 'SP000550'}
        {'dfem_evidence': '[推力轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽油黏度]实测值(43.79)超低限报警,阈值43.70', 'dfem_code': 'SP000550'}
        {'dfem_evidence': '[推力轴承油槽油黏度]实测值(43.79)超低限报警,阈值43.70', 'dfem_code': 'SP000550'}
        {'dfem_evidence': '[推力轴承油槽油黏度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽油黏度]实测值(43.70)超低限报警,阈值43.70', 'dfem_code': 'SP000550'}
        {'dfem_evidence': '[推力轴承油槽油黏度]正常', 'dfem_code': ''}
    """
    np.random.seed(1234)
    tempers = (np.random.randn(10, 1) * 0.1 + 43.7).flatten().tolist()
    obj = ThrustBearingOilViscosityOverLimitDiagnosis()
    for i in tempers:
        print(obj.diagnosis(i))


if __name__ == '__main__':
    main()
