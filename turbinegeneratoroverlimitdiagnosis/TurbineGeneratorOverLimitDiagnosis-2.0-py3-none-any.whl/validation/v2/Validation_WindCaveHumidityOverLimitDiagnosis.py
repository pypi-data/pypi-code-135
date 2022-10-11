from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WindCaveHumidityOverLimitDiagnosis import WindCaveHumidityOverLimitDiagnosis
# from tools.v2.Method_WindCaveHumidityOverLimitDiagnosis import WindCaveHumidityOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[风洞内湿度]实测值(0.10)正常,阈值0.75', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内湿度]实测值(0.70)正常,阈值0.75', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内湿度]实测值(1.00)超限,阈值0.75', 'dfem_code': 'SP000160'}
        {'dfem_evidence': '[风洞内湿度]实测值(2.00)超限,阈值0.75', 'dfem_code': 'SP000160'}
    """
    obj = WindCaveHumidityOverLimitDiagnosis()
    for item in [0.1, 0.7, 1, 2]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()