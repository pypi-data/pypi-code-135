# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorWindingTemperOverLimitDiagnosis import StatorWindingTemperOverLimitDiagnosis
from tools.v2.Method_StatorWindingTemperOverLimitDiagnosis import StatorWindingTemperOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[定子绕组运行温度]不超限', 'dfem_code': ''}
        {'dfem_evidence': '[定子绕组运行温度]不超限', 'dfem_code': ''}
        {'dfem_evidence': '[定子绕组运行温度]实测值(113.00)一级超限,阈值110.00', 'dfem_code': 'SP000001'}
        {'dfem_evidence': '[定子绕组运行温度]实测值(123.00)一级超限,阈值110.00', 'dfem_code': 'SP000001'}
        {'dfem_evidence': '[定子绕组运行温度]实测值(133.00)二级超限,阈值125.00', 'dfem_code': 'SP000002'}
    """
    obj = StatorWindingTemperOverLimitDiagnosis()
    for item in [90, 100, 113, 123, 133]:
        print(obj.diagnosis(item))


if __name__=="__main__":
    main()