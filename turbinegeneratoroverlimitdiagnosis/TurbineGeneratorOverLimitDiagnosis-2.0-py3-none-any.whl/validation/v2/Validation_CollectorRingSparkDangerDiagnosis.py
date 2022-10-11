from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_CollectorRingSparkDangerDiagnosis import CollectorRingSparkDangerDiagnosis
# from tools.v2.Method_CollectorRingSparkDangerDiagnosis import CollectorRingSparkDangerDiagnosis

import numpy as np

def main():
    """
    output:
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 5)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 2)正常,阈值 3', 'dfem_code': ''}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 2)正常,阈值 3', 'dfem_code': ''}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 2)正常,阈值 3', 'dfem_code': ''}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 1)正常,阈值 3', 'dfem_code': ''}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 2)正常,阈值 3', 'dfem_code': ''}, [], []
        {'dfem_evidence': '[集电环异常打火]连续周期极值数量( 3)超限,阈值 3', 'dfem_code': 'SP000400'}, [], []
    """
    obj = CollectorRingSparkDangerDiagnosis(roundingFormat="%2d")

    avgs = (100 + np.random.randn(100, 1)).tolist()
    maxs = (150 + np.random.randn(100, 1)).tolist()

    avgTemperBuffer, maxTemperBuffer = [], []
    for item in zip(avgs, maxs):
        count, avgTemperBuffer, maxTemperBuffer = obj.diagnosis(*item[0], *item[1], avgTemperBuffer, maxTemperBuffer)
        if isinstance(count, dict):
            print(f"{count}")


if __name__ == '__main__':
    main()