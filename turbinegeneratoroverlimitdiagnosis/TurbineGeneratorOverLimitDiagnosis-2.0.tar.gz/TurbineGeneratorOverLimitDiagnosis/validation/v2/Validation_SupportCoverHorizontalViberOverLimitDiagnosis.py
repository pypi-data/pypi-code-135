# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_SupportCoverHorizontalVibrationOverLimitDiagnosis import SupportCoverHorizontalViberOverLimitDiagnosis
from tools.v2.Method_SupportCoverHorizontalVibrationOverLimitDiagnosis import SupportCoverHorizontalViberOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[支持盖振动]正常', 'dfem_code': ''}
        {'dfem_evidence': '[支持盖振动]实测值(0.07)超限一级报警,阈值0.07', 'dfem_code': 'SP000141'}
        {'dfem_evidence': '[支持盖振动]实测值(0.09)超限一级报警,阈值0.07', 'dfem_code': 'SP000141'}
        {'dfem_evidence': '[支持盖振动]实测值(0.10)超限二级报警,阈值0.09', 'dfem_code': 'SP000142'}
    """

    truthTable = {
        "100": {"dfem_evidence": "[支持盖振动]正常", "dfem_code": ""},
        "010": {"dfem_evidence": "[支持盖振动]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000141"},
        "001": {"dfem_evidence": "[支持盖振动]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000142"},
    }

    obj = SupportCoverHorizontalViberOverLimitDiagnosis([0.07, 0.09], truthTable, roundingFormat="%2.2f")
    for item in [0.01, 0.075, 0.085, 0.095]:
        print(obj.diagnosis(item))


if __name__ == '__main__':
    main()