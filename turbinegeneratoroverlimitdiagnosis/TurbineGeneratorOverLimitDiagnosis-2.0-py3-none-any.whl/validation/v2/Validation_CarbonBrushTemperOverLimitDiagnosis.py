from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_CarbonBrushTemperOverLimitDiagnosis import CarbonBrushTemperOverLimitDiagnosis
# from tools.v2.Method_CarbonBrushTemperOverLimitDiagnosis import CarbonBrushTemperOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[碳刷温度]实测值(100.00)正常,阈值125.00', 'dfem_code': ''}
        {'dfem_evidence': '[碳刷温度]实测值(120.00)正常,阈值125.00', 'dfem_code': ''}
        {'dfem_evidence': '[碳刷温度]实测值(130.00)超限,阈值125.00', 'dfem_code': 'SP000190'}
        {'dfem_evidence': '[碳刷温度]实测值(200.00)超限,阈值125.00', 'dfem_code': 'SP000190'}
    """
    obj = CarbonBrushTemperOverLimitDiagnosis()
    for item in [100, 120, 130, 200]:
        print(obj.diagnosis(item))
if __name__ == '__main__':
    main()