from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingPadTemperOverLimitDiagnosis import UpperGuideBearingPadTemperOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingPadTemperOverLimitDiagnosis import UpperGuideBearingPadTemperOverLimitDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承瓦温]实测值(75.47)超限一级报警,阈值75.00', 'dfem_code': 'SP000431'}
        {'dfem_evidence': '[上导轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承瓦温]实测值(76.43)超限一级报警,阈值75.00', 'dfem_code': 'SP000431'}
        {'dfem_evidence': '[上导轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承瓦温]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承瓦温]实测值(85.89)超限二级报警,阈值85.00', 'dfem_code': 'SP000432'}
        {'dfem_evidence': '[上导轴承瓦温]实测值(85.86)超限二级报警,阈值85.00', 'dfem_code': 'SP000432'}
        {'dfem_evidence': '[上导轴承瓦温]实测值(84.36)超限一级报警,阈值75.00', 'dfem_code': 'SP000431'}
        {'dfem_evidence': '[上导轴承瓦温]实测值(85.02)超限二级报警,阈值85.00', 'dfem_code': 'SP000432'}
        {'dfem_evidence': '[上导轴承瓦温]实测值(82.76)超限一级报警,阈值75.00', 'dfem_code': 'SP000431'}
    """
    np.random.seed(1234)
    tempers = (np.random.randn(5, 1) + 75).flatten().tolist() + (np.random.randn(5, 1) + 85).flatten().tolist()

    obj = UpperGuideBearingPadTemperOverLimitDiagnosis()
    for i in tempers:
        print(
            obj.diagnosis(i)
        )


if __name__ == '__main__':
    main()