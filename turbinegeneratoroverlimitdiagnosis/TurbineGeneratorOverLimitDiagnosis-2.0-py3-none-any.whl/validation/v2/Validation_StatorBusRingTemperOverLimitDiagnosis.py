# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_StatorBusRingTemperOverLimitDiagnosis import StatorBusRingTemperOverLimitDiagnosis
from tools.v2.Method_StatorBusRingTemperOverLimitDiagnosis import StatorBusRingTemperOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[定子汇流环温度]不超限', 'dfem_code': ''}
        {'dfem_evidence': '[定子汇流环温度]实测值(1100.00)二级超限,阈值125.00', 'dfem_code': 'SP000002'}
        {'dfem_evidence': '[定子汇流环温度]不超限', 'dfem_code': ''}
        {'dfem_evidence': '[定子汇流环温度]实测值(123.00)一级超限,阈值110.00', 'dfem_code': 'SP000001'}
        {'dfem_evidence': '[定子汇流环温度]实测值(133.00)二级超限,阈值125.00', 'dfem_code': 'SP000002'}
    """
    obj = StatorBusRingTemperOverLimitDiagnosis()
    for item in [90, 1100, 13, 123, 133]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()