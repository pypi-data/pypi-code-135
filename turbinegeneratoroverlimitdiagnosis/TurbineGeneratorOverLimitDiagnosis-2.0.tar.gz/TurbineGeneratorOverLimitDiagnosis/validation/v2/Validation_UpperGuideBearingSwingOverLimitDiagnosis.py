from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingSwingOverLimitDiagnosis import UpperGuideBearingSwingOverLimitDiagnosis
# from tools.v2.Method_UpperGuideBearingSwingOverLimitDiagnosis import UpperGuideBearingSwingOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[上导摆度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导摆度]运行值(0.18)超限一级报警,阈值0.15', 'dfem_code': 'SP000101'}
        {'dfem_evidence': '[上导摆度]运行值(0.30)超限二级报警,阈值0.20', 'dfem_code': 'SP000102'}
    """
    obj = UpperGuideBearingSwingOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.1, 0.18, 0.3]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()