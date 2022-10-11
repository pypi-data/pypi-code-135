from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_ThrustBearingPadDegradedDegreeDiagnosis import ThrustBearingPadDegradedDegreeDiagnosis
# from tools.v2.Method_ThrustBearingPadDegradedDegreeDiagnosis import ThrustBearingPadDegradedDegreeDiagnosis

import numpy as np


def main():
    """
    output:
        {'dfem_evidence': '[推力轴承瓦瓦面润滑情况]劣化正常', 'dfem_code': ''}
        ......
        {'dfem_evidence': '[推力轴承瓦瓦面润滑情况]劣化正常', 'dfem_code': ''}
        {'dfem_evidence': '[推力轴承瓦面]劣化程度(8.27)超限报警,阈值0.10', 'dfem_code': 'SP000630'}
        {'dfem_evidence': '[推力轴承瓦面]劣化程度(8.27)超限报警,阈值0.10', 'dfem_code': 'SP000630'}
        {'dfem_evidence': '[推力轴承瓦面]劣化程度(8.27)超限报警,阈值0.10', 'dfem_code': 'SP000630'}
        {'dfem_evidence': '[推力轴承瓦面]劣化程度(8.27)超限报警,阈值0.10', 'dfem_code': 'SP000630'}
        {'dfem_evidence': '[推力轴承瓦面]劣化程度(8.27)超限报警,阈值0.10', 'dfem_code': 'SP000630'}
        {'dfem_evidence': '[推力轴承瓦瓦面润滑情况]劣化正常', 'dfem_code': ''}
        ......
        {'dfem_evidence': '[推力轴承瓦瓦面润滑情况]劣化正常', 'dfem_code': ''}
    """
    np.random.seed(1234)
    values = np.random.randn(130, 1)
    timestamps = np.arange(1665368444, 1665368444 + 130).reshape((130, 1))
    samples = np.concatenate([values, timestamps], axis=1)
    obj = ThrustBearingPadDegradedDegreeDiagnosis(theoreticIncreaseRate=0.5)
    for i in range(len(samples)):
        print(obj.diagnosis(*samples[i]))


if __name__ == '__main__':
    main()
