from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WhichCarbonBrushTemperOverLimitDiagnosis import WhichCarbonBrushTemperOverLimitDiagnosis
# from tools.v2.Method_WhichCarbonBrushTemperOverLimitDiagnosis import WhichCarbonBrushTemperOverLimitDiagnosis

import numpy as np

def main():
    """
    output形如:
    [
        {'dfem_evidence': '[第1号碳刷温度]偏差(-0.97)正常,阈值0.20', 'dfem_code': 'SP000201'},
        ……
        {'dfem_evidence': '[第63号碳刷温度]偏差(0.24)异常,阈值0.20', 'dfem_code': 'SP000263'}
    ]
    """
    obj = WhichCarbonBrushTemperOverLimitDiagnosis()
    for item in range(3):
        print(obj.diagnosis(
            {"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(), "seq": np.arange(1, 33)},
            {"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(), "seq": np.arange(33, 65)})
        )


if __name__ == '__main__':
    main()