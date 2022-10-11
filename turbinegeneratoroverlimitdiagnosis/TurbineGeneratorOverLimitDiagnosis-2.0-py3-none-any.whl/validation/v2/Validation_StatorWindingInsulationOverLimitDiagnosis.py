# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorWindingInsulationOverLimitDiagnosis import StatorWindingInsulationOverLimitDiagnosis
from tools.v2.Method_StatorWindingInsulationOverLimitDiagnosis import StatorWindingInsulationOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[定子绕组绝缘劣化]实测值(0.50)二级报警,阈值0.80', 'dfem_code': 'SP000042'}
        {'dfem_evidence': '[定子绕组绝缘劣化]实测值(0.70)一级报警,阈值0.60', 'dfem_code': 'SP000041'}
        {'dfem_evidence': '[定子绕组绝缘劣化]不超限', 'dfem_code': ''}
        {'dfem_evidence': '[定子绕组绝缘劣化]不超限', 'dfem_code': ''}
    """
    obj = StatorWindingInsulationOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.5, 0.7, 0.9, 2]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()