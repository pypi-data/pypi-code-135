# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WhichCarbonBrushCurrentOverLimitDiagnosis import WhichCarbonBrushCurrentOverLimitDiagnosis
from tools.v2.Method_WhichCarbonBrushCurrentOverLimitDiagnosis import WhichCarbonBrushCurrentOverLimitDiagnosis
import numpy as np


def main():
    """
    output形如:
    [
        {'dfem_evidence': '[第1号碳刷负载电流]偏差(-0.53)正常,阈值0.30', 'dfem_code': ''},

        {'dfem_evidence': '[第2号碳刷负载电流]偏差(1.51)异常,阈值0.30', 'dfem_code': 'SP000302)'},

        ...
    ]
    """
    obj = WhichCarbonBrushCurrentOverLimitDiagnosis()
    for item in range(1):
        print(obj.diagnosis(
            {"currents": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(),
             "seq": np.arange(1, 33)},
            {"currents": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(), "seq": np.arange(33, 65)})
        )


if __name__ == '__main__':
    main()