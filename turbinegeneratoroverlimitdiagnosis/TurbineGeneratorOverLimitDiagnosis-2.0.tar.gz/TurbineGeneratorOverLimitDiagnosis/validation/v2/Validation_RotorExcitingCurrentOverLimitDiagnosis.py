from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_RotorExcitingCurrentOverLimitDiagnosis import RotorExcitingCurrentOverLimitDiagnosis
# from tools.v2.Method_RotorExcitingCurrentOverLimitDiagnosis import RotorExcitingCurrentOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[转子励磁电流]正常', 'dfem_code': ''}
        {'dfem_evidence': '[转子励磁电流]运行值(0.20)异常,阈值0.15', 'dfem_code': 'SP000081'}
        {'dfem_evidence': '[转子励磁电流]运行值(0.30)异常,阈值0.15', 'dfem_code': 'SP000081'}
    """
    obj = RotorExcitingCurrentOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.1, 0.2, 0.3]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()