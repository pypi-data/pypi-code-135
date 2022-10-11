from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingOilTankTemperOverLimitDiagnosis import ThrustBearingOilTankTemperOverLimitDiagnosis
# from tools.v2.Method_ThrustBearingOilTankTemperOverLimitDiagnosis import ThrustBearingOilTankTemperOverLimitDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承油槽温度]实测值(45.47)超限一级报警,阈值45.00', 'dfem_code': 'SP000531'}
        {'dfem_evidence': '[推力轴承油槽温度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(46.43)超限一级报警,阈值45.00', 'dfem_code': 'SP000531'}
        {'dfem_evidence': '[推力轴承油槽温度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽温度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(50.89)超限二级报警,阈值50.00', 'dfem_code': 'SP000532'}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(50.86)超限二级报警,阈值50.00', 'dfem_code': 'SP000532'}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(49.36)超限一级报警,阈值45.00', 'dfem_code': 'SP000531'}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(50.02)超限二级报警,阈值50.00', 'dfem_code': 'SP000532'}
        {'dfem_evidence': '[推力轴承油槽温度]实测值(47.76)超限一级报警,阈值45.00', 'dfem_code': 'SP000531'}
    """
    np.random.seed(1234)
    tempers = (np.random.randn(5, 1) + 45).flatten().tolist() + (np.random.randn(5, 1) + 50).flatten().tolist()
    obj = ThrustBearingOilTankTemperOverLimitDiagnosis()
    for i in tempers:
        print(obj.diagnosis(i))


if __name__ == '__main__':
    main()
