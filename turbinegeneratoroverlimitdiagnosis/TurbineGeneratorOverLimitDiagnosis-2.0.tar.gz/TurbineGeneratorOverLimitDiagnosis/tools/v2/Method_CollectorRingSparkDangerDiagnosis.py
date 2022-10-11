from .GenericMethods import *


class CollectorRingSparkDangerDiagnosis:
    def __init__(self, **kwargs):
        """
        集电环存在打火隐患评估

        D为连续周期极值点数量

        :math:`D < 3, 集电环未出现异常打火`

        :math:`D ≥ 3, 集电环存在打火隐患`

        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[3]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)正常,阈值threshold", "dfem_code": ""},

                    "01": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)超限,阈值threshold", "dfem_code": "SP000400"},
                }
        roundingFormat:
            str, 数值精度格式,默认"%2.2f"

        [2] 方法
        ----------
        diagnosis:
            判断当前输入对判断逻辑的满足情况

        [3] 返回
        -------
        -/-:
            超限判断结论

        [4] 示例1
        --------
        >>> truthTable = {
        >>>     "10": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)正常,阈值threshold", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)超限,阈值threshold", "dfem_code": "SP000400"},
        >>> }
        >>> obj = CollectorRingSparkDangerDiagnosis(roundingFormat="%2d")
        >>> avgs = (100+np.random.randn(100, 1)).tolist()
        >>> maxs = (150+np.random.randn(100, 1)).tolist()
        >>> avgTemperBuffer, maxTemperBuffer = [], []
        >>> for item in zip(avgs, maxs):
        >>>     count, avgTemperBuffer, maxTemperBuffer = obj.diagnosis(*item[0], *item[1], avgTemperBuffer, maxTemperBuffer)
        >>>     if isinstance(count, dict):
        >>>         print(f">>> {count}, {avgTemperBuffer}, {maxTemperBuffer}")

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        _defaultTruthTable = {
            "10": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)正常,阈值threshold", "dfem_code": ""},
            "01": {"dfem_evidence": "[集电环异常打火]连续周期极值数量(measured)超限,阈值threshold", "dfem_code": "SP000400"},
        }
        self.truthTable = kwargs["truthTable"] if "truthTable" in kwargs.keys() else _defaultTruthTable
        self.thresholds = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [3]
        self.roundingFormat = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        self.overLimitPercentage = kwargs["overLimitPercentage"] if "overLimitPercentage" in kwargs.keys() else 0.5
        self.continuousPeriodsQuant = kwargs["continuousPeriodsQuant"] if "continuousPeriodsQuant" in kwargs.keys() else 6
        self.obj = MultipleThresholds_GreaterEqualTo_LesserThan(self.thresholds, self.truthTable, roundingFormat=self.roundingFormat)

    def diagnosis(self, avgTemper, maxTemper, avgTemperBuffer, maxTemperBuffer):
        """
        判断是否存在打火隐患

        :param avgTemper: 本周期均值
        :type avgTemper: float

        :param maxTemper: 本周期最大值
        :type maxTemper: float

        :param avgTemperBuffer: 近期均值缓存
        :type avgTemperBuffer: list[float]

        :param maxTemperBuffer: 近期最大值缓存
        :type maxTemperBuffer: list[float]
        :return: (判断结论, 均值缓存, 最大值缓存)
        """
        if len(avgTemperBuffer) < self.continuousPeriodsQuant:
            avgTemperBuffer.append(avgTemper)
            maxTemperBuffer.append(maxTemper)
            return np.nan, avgTemperBuffer, maxTemperBuffer
        elif len(avgTemperBuffer) == self.continuousPeriodsQuant:
            avgTemperBuffer = avgTemperBuffer[1:]
            maxTemperBuffer = maxTemperBuffer[1:]
            # 判断
            count = np.where(np.divide(np.subtract(maxTemperBuffer, avgTemperBuffer), avgTemperBuffer) > self.overLimitPercentage)
            avgTemperBuffer, maxTemperBuffer = [], []
            res = self.obj.diagnosis(count[0].shape[0])
            return res, avgTemperBuffer, maxTemperBuffer
        else:
            pass




