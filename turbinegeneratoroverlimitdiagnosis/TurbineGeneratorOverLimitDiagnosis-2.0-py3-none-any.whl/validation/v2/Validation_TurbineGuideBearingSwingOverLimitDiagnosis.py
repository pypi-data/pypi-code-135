from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_TurbineGuideBearingSwingOverLimitDiagnosis import TurbineGuideBearingSwingOverLimitDiagnosis
# from tools.v2.Method_TurbineGuideBearingSwingOverLimitDiagnosis import TurbineGuideBearingSwingOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[水导摆度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[水导摆度]运行值(0.18)超限一级报警,阈值0.18', 'dfem_code': 'SP000111'}
        {'dfem_evidence': '[水导摆度]运行值(0.30)超限二级报警,阈值0.23', 'dfem_code': 'SP000112'}
    """
    truthTable = {
        "100": {"dfem_evidence": "[水导摆度]正常", "dfem_code": ""},
        "010": {"dfem_evidence": "[水导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000111"},
        "001": {"dfem_evidence": "[水导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000112"},
    }

    obj = TurbineGuideBearingSwingOverLimitDiagnosis([0.18, 0.23], truthTable, roundingFormat="%2.2f")
    for item in [0.1, 0.18, 0.3]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()