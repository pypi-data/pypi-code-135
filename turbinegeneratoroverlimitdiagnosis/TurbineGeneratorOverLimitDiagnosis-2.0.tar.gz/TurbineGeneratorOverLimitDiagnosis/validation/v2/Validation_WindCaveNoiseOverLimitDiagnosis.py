from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WindCaveNoiseOverLimitDiagnosis import WindCaveNoiseOverLimitDiagnosis
# from tools.v2.Method_WindCaveNoiseOverLimitDiagnosis import WindCaveNoiseOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[风洞内噪声水平]实测值(-6.47)正常,阈值85.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内噪声水平]实测值(3.53)正常,阈值85.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内噪声水平]实测值(13.53)正常,阈值85.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内噪声水平]实测值(69.03)正常,阈值85.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内噪声水平]实测值(89.40)超限,阈值85.00', 'dfem_code': 'SP000170'}
    """
    for item in [(1, 2), (11, 12), (21, 22), (60, 80), (100, 90)]:
        obj = WindCaveNoiseOverLimitDiagnosis(item, Klis=[4, 4], K2=4)
        print(obj.diagnosis())

if __name__ == '__main__':
    main()