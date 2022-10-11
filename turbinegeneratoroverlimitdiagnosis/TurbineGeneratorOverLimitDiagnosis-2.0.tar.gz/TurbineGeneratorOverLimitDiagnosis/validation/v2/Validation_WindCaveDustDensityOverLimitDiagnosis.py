from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WindCaveDustDensityOverLimitDiagnosis import WindCaveDustDensityOverLimitDiagnosis
# from tools.v2.Method_WindCaveDustDensityOverLimitDiagnosis import WindCaveDustDensityOverLimitDiagnosis


def main():
    """
    output:
        {'dfem_evidence': '[风洞内粉尘浓度]实测值(1.00)正常,阈值100.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内粉尘浓度]实测值(90.00)正常,阈值100.00', 'dfem_code': ''}
        {'dfem_evidence': '[风洞内粉尘浓度]实测值(101.00)超限,阈值100.00', 'dfem_code': 'SP000150'}
        {'dfem_evidence': '[风洞内粉尘浓度]实测值(200.00)超限,阈值100.00', 'dfem_code': 'SP000150'}
    """
    obj = WindCaveDustDensityOverLimitDiagnosis()
    for item in [1, 90, 101, 200]:
        print(obj.diagnosis(item))

if __name__ == '__main__':
    main()