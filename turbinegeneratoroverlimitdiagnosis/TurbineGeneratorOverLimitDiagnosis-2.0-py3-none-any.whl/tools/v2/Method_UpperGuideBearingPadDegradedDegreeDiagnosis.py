import pandas as pd

from .GenericMethods import *


class UpperGuideBearingPadDegradedDegreeDiagnosis:
    def __init__(self, *args, **kwargs):
        """
        上导轴承瓦瓦面劣化程度评估

        :math:`T < 0.1, 上导轴承瓦面润滑情况劣化正常`

        :math:`0.1 ≤ T, 上导轴承瓦面劣化程度超限`

        [1] 参数
        ----------
        theoreticIncreaseRate:
            list[float],温度上升率理论值,℃/min
        thresholds:
            list[float],报警限,默认[0.1]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[上导轴承瓦瓦面润滑情况]劣化正常", "dfem_code": ""},
                    "01": {"dfem_evidence": "[上导轴承瓦面]劣化程度(measured)超限报警,阈值threshold", "dfem_code": "SP000510"},
                }

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
        >>> np.random.seed(1234)
        >>> values = np.random.randn(130, 1)
        >>> timestamps = np.arange(1665368444, 1665368444+130).reshape((130, 1))
        >>> samples = np.concatenate([values, timestamps], axis=1)
        >>> obj = UpperGuideBearingPadDegradedDegreeDiagnosis(theoreticIncreaseRate=5)
        >>> for i in range(len(samples)):
        >>>     print(obj.diagnosis(*samples[i]))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        thresholds = [0.1]
        truthTable = {
            "10": {"dfem_evidence": "[上导轴承瓦瓦面润滑情况]劣化正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[上导轴承瓦面]劣化程度(measured)超限报警,阈值threshold", "dfem_code": "SP000510"},
        }
        if not "theoreticIncreaseRate" in kwargs.keys():
            raise Exception("缺少温度上升率理论值[theoreticIncreaseRate]")
        else:
            self.theoreticIncreaseRate = kwargs["theoreticIncreaseRate"]
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else thresholds
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else truthTable
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        kwargs.pop("theoreticIncreaseRate")
        self.__obj = MultipleThresholds_GreaterEqualTo_LesserThan(*args, **kwargs)
        self.buffer = pd.DataFrame({})

    def diagnosis(self, padTemper: float, timestamp: float):
        """
        判断

        判据是上导轴瓦瓦温上升率℃/min(参考上导轴瓦润滑性能评估中,关于上升率的计算方式),即,一分钟内第一个最小值与最后一个最大值的差值
        默认缓存时间长度为120s

        :param padTemper: 瓦温
        :type padTemper: float

        :param timestamp: unix时间戳
        :type timestamp: float
        :return: dict,判断结论
        """
        # 更新缓存
        _sample = pd.DataFrame({"value": [padTemper], "timestamp": [timestamp]})
        self.buffer = pd.concat([self.buffer, _sample], axis=0)
        # 上升率计算
        increaseRate = 0
        values = self.buffer["value"].values.flatten().tolist()
        ts = self.buffer["timestamp"].values.flatten().tolist()
        if ts[-1] - ts[0] >= 60:
            _max, _min = max(values), min(values)
            _maxLoc, _minLoc = np.where(np.asarray(values) == _max)[0], np.where(np.asarray(values) == _min)[0]
            if _maxLoc[-1] > _minLoc[0]:
                increaseRate = _max - _min
        # 缓存尺寸控制
        self.buffer = self.buffer.where(self.buffer["timestamp"]>=(timestamp - 120)).dropna()
        # 温度上升率与理论值偏差
        increaseRate_bias = (increaseRate - self.theoreticIncreaseRate) / self.theoreticIncreaseRate
        return self.__obj.diagnosis(increaseRate_bias)
