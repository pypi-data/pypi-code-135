from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_AirCoolerDegradedDegreeDiagnosis import AirCoolerDegradedDegreeDiagnosis
# from tools.v2.Method_AirCoolerDegradedDegreeDiagnosis import AirCoolerDegradedDegreeDiagnosis

import numpy as np

def main():
    """
    output:
        {
            'dfem_evidence': [
                        '[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似',
                        '[第4号空冷器]运行异常(0.11),阈值0.10', '[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似',
                        '[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似',
                        '[第10号空冷器]运行异常(0.12),阈值0.10'
                    ],
            'dfem_code': [
                        '', '', '', 'SP000424', '', '', '', '', '', 'SP0004210'
                    ]
        }
    """
    np.random.seed(1234)
    a1 = np.random.randn(10, 1) + 70
    a2 = np.random.randn(10, 1) + 82
    a3 = np.random.randn(10, 1) + 85
    a4 = np.random.randn(10, 1) + 86
    a = np.concatenate([a1, a2, a3, a4], axis=1)

    obj = AirCoolerDegradedDegreeDiagnosis()
    for i in range(1):
        print(
            obj.diagnosis(a)
        )


if __name__ == '__main__':
    main()