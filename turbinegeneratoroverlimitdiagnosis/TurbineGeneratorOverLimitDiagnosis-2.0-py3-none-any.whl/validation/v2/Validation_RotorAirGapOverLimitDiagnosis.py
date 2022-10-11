from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_RotorAirGapOverLimitDiagnosis import RotorAirGapOverLimitDiagnosis
# from tools.v2.Method_RotorAirGapOverLimitDiagnosis import RotorAirGapOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[转子气隙]运行值(0.10)异常,阈值0.04', 'dfem_code': 'SP000091'}
        {'dfem_evidence': '[转子气隙]运行值(0.20)异常,阈值0.04', 'dfem_code': 'SP000091'}
        {'dfem_evidence': '[转子气隙]正常', 'dfem_code': ''}
    """
    obj = RotorAirGapOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.1, 0.2, 0.03]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()