from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_RotorTemperOverLimitDiagnosis import RotorTemperOverLimitDiagnosis
# from tools.v2.Method_RotorTemperOverLimitDiagnosis import RotorTemperOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[转子运行温度]正常', 'dfem_code': ''}
        {'dfem_evidence': '[转子运行温度]实测值(120.00)一级报警,阈值110.00', 'dfem_code': 'SP000071'}
        {'dfem_evidence': '[转子运行温度]实测值(130.00)二级报警,阈值125.00', 'dfem_code': 'SP000072'}
    """
    obj = RotorTemperOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [100, 120, 130]:
        print(obj.diagnosis(item))


if __name__ == '__main__':
    main()