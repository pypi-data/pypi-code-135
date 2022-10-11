from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorUpperFrameHorizontalVibrationOverLimitDiagnosis import StatorUpperFrameHorizontalViberOverLimitDiagnosis
# from tools.v2.Method_StatorUpperFrameHorizontalVibrationOverLimitDiagnosis import StatorUpperFrameHorizontalViberOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[上机架振动]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上机架振动]实测值(0.07)超限一级报警,阈值0.07', 'dfem_code': 'SP000131'}
        {'dfem_evidence': '[上机架振动]实测值(0.09)超限二级报警,阈值0.08', 'dfem_code': 'SP000132'}
    """
    obj = StatorUpperFrameHorizontalViberOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.01, 0.075, 0.085]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()