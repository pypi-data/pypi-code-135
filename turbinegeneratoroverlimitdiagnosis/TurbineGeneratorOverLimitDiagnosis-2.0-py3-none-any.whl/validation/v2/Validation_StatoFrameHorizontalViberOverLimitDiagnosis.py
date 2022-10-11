from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorFrameHorizontalVibrationOverLimitDiagnosis import StatorFrameHorizontalViberOverLimitDiagnosis
# from tools.v2.Method_StatorFrameHorizontalVibrationOverLimitDiagnosis import StatorFrameHorizontalViberOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[定子机座振动]正常', 'dfem_code': ''}
        {'dfem_evidence': '[定子机座振动]实测值(0.04)超限一级报警,阈值0.03', 'dfem_code': 'SP000121'}
        {'dfem_evidence': '[定子机座振动]实测值(0.04)超限二级报警,阈值0.04', 'dfem_code': 'SP000122'}
    """
    obj = StatorFrameHorizontalViberOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.01, 0.035, 0.043]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()