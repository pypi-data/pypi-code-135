from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WhichThrustBearingPadAbnormalStressDiagnosis import WhichThrustBearingPadAbnormalStressDiagnosis
# from tools.v2.Method_WhichThrustBearingPadAbnormalStressDiagnosis import WhichThrustBearingPadAbnormalStressDiagnosis

import numpy as np


def main():
    """
    output:
        {
            'dfem_evidence': [
                '[第1号推力轴瓦受力]温度偏差计算值(0.90)异常,阈值0.04',
                '[第2号推力轴瓦受力]正常',
                '[第3号推力轴瓦受力]温度偏差计算值(0.28)异常,阈值0.04',
                ...
            ],
            'dfem_code': [
                'SP000701',
                '',
                'SP000703',
                ...
            ]
        }

    """
    obj = WhichThrustBearingPadAbnormalStressDiagnosis()
    for item in range(1):
        print(
            obj.diagnosis({"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(),
                           "seq": np.arange(1, 33)})
        )


if __name__ == '__main__':
    main()
