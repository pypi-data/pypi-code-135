from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorCoreVibrationOverLimitDiagnosis import StatorCoreVibrationOverLimitDiagnosis
# from tools.v2.Method_StatorCoreVibrationOverLimitDiagnosis import StatorCoreVibrationOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[定子铁芯振动]正常', 'dfem_code': ''}
        {'dfem_evidence': '[定子铁芯振动]实测值(0.07)指标超限,阈值0.03', 'dfem_code': 'SP000051'}
        {'dfem_evidence': '[定子铁芯振动]实测值(0.09)指标超限,阈值0.03', 'dfem_code': 'SP000051'}
        {'dfem_evidence': '[定子铁芯振动]正常', 'dfem_code': ''}
    """
    obj = StatorCoreVibrationOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.005, 0.07, 0.09, 0.0002]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()