from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingPadTemperOverLimitDiagnosis import ThrustBearingPadTemperOverLimitDiagnosis
# from tools.v2.Method_ThrustBearingPadTemperOverLimitDiagnosis import ThrustBearingPadTemperOverLimitDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.47)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]实测值(76.43)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.89)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.86)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.02)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]实测值(76.15)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.99)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.95)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.00)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.41)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(75.29)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]实测值(76.32)超限一级报警,阈值75.00', 'dfem_code': 'SP000521'}
        {'dfem_evidence': '[推力轴承瓦温]正常', 'dfem_code': ''}

    """
    np.random.seed(1234)
    tempers = list((np.random.randn(20, 1)+75).flatten())
    obj = ThrustBearingPadTemperOverLimitDiagnosis()
    for item in tempers:
        print(obj.diagnosis(item))


if __name__ == '__main__':
    main()
