from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_UpperGuideBearingPadLubricationPerformanceDiagnosis import UpperGuideBearingPadLubricationPerformanceDiagnosis
# from tools.v2.Method_UpperGuideBearingPadLubricationPerformanceDiagnosis import UpperGuideBearingPadLubricationPerformanceDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[上导轴承瓦面润滑性能]正常', 'dfem_code': ''}
        ......
        {'dfem_evidence': '[上导轴承瓦面润滑性能]正常', 'dfem_code': ''}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]轴瓦温度上升率计算值(4.63)超限报警,阈值1.20', 'dfem_code': 'SP000500'}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]轴瓦温度上升率计算值(4.63)超限报警,阈值1.20', 'dfem_code': 'SP000500'}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]轴瓦温度上升率计算值(4.63)超限报警,阈值1.20', 'dfem_code': 'SP000500'}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]轴瓦温度上升率计算值(4.63)超限报警,阈值1.20', 'dfem_code': 'SP000500'}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]轴瓦温度上升率计算值(4.63)超限报警,阈值1.20', 'dfem_code': 'SP000500'}
        {'dfem_evidence': '[上导轴承瓦面润滑性能]正常', 'dfem_code': ''}
        ......
        {'dfem_evidence': '[上导轴承瓦面润滑性能]正常', 'dfem_code': ''}
    """
    np.random.seed(1234)
    values = np.random.randn(130, 1)
    timestamps = np.arange(1665368444, 1665368444 + 130).reshape((130, 1))
    samples = np.concatenate([values, timestamps], axis=1)
    obj = UpperGuideBearingPadLubricationPerformanceDiagnosis()
    for i in range(len(samples)):
        print(obj.diagnosis(*samples[i]))


if __name__ == '__main__':
    main()