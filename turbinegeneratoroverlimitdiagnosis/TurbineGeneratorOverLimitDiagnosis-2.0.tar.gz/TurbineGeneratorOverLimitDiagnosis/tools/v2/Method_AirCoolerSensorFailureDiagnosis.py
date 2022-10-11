import pandas as pd
from .GenericMethods import *


def ExtremePointFinder(time: list, value: list):
    _extremeTimes = []
    _extremeValues = []
    _dataLength = len(value)
    for item in range(1, _dataLength - 1):
        _data = value[(item - 1):(item + 2)]
        _time = time[(item - 1):(item + 2)]
        if (_data[1] > _data[0]) and (_data[1] > _data[-1]):  # 极大值点
            _extremeValues.append(_data[1])
            _extremeTimes.append(_time[1])
        elif (_data[1] < _data[0]) and (_data[1] < _data[-1]):  # 极小值点
            _extremeValues.append(_data[1])
            _extremeTimes.append(_time[1])
    return _extremeTimes, _extremeValues

def PotentialExtremePointFinder(time: list, value: list):
    _extremeTimes = []
    _extremeValues = []
    _dataLength = len(value)
    if value[_dataLength-1] != value[_dataLength-2]:
        _extremeTimes.append(time[_dataLength-1])
        _extremeValues.append(value[_dataLength-1])
    return _extremeTimes, _extremeValues

class TruthTable:
    def __init__(self):
        self.temperOverLimitFault_truthTable = {
            "10": {"dfem_evidence": "", "dfem_code": ""},
            "01": {"dfem_evidence": "[空冷器温度]传感器温度超限故障(measured),阈值threshold$(group01)", "dfem_code": "SP000410"},
        }
        self.peakQuantOverLimitFault_truthTable = {
                "10": {"dfem_evidence": "", "dfem_code": ""},
                "01": {"dfem_evidence": "[空冷器温度]传感器极值点数量超限故障(measured),阈值threshold$(group02)", "dfem_code": "SP000411"},
        }
        self.peak2PeakOverLimitFault_truthTable = {
                "10": {"dfem_evidence": "[空冷器温度]传感器峰峰值过小故障(measured),阈值threshold$(group03)", "dfem_code": "SP000412"},
                "01": {"dfem_evidence": "", "dfem_code": ""},
        }


class AirCoolerSensorFailureDiagnosis:
    def __init__(self, **kwargs):
        """
        通风冷却系统传感器故障判断

        [1] 参数
        ----------
        maximumTimeRange:
            float,计算峰峰值的时间窗口长度(最大缓存时间),秒,默认3600*24
        minimumTimeRange:
            float,计算极值点数量的时间窗口长度,秒,默认60*10
        neighboringPeakMinimumHeight:
            float,相邻两个极值点的最小允许差值,℃,默认2
        realtimeTemperThreshold:
            float,实时温度最大允许值,℃,默认205
        historyTemperDiffThreshold:
            float,峰峰值温度最小允许值(小于此值即认为传感器失效),℃,默认0.2
        extremePointQuantThreshold:
            int,合法的相邻极值点数量,默认5

        temperOverLimitFault_truthTable:
            dict,报警真值表,默认{
            "10": {"dfem_evidence": "", "dfem_code": ""},
            "01": {"dfem_evidence": "[空冷器温度]传感器温度超限故障(measured),阈值threshold$(group01)", "dfem_code": "SP000410"}
        }

        peakQuantOverLimitFault_truthTable:
            dict,报警真值表,默认{
                "10": {"dfem_evidence": "", "dfem_code": ""},
                "01": {"dfem_evidence": "[空冷器温度]传感器极值点数量超限故障(measured),阈值threshold$(group02)", "dfem_code": "SP000411"}
        }

        peak2PeakOverLimitFault_truthTable:
            dict,报警真值表,默认{
                "10": {"dfem_evidence": "[空冷器温度]传感器峰峰值过小故障(measured),阈值threshold$(group03)", "dfem_code": "SP000412"}
                "01": {"dfem_evidence": "", "dfem_code": ""},
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
        >>> extremeQuantOverLimit_values = [
        >>>     80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88,
        >>>     90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>>     80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
        >>>     80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>>     90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 280, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>>     80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88,
        >>>     90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>>     80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
        >>>     80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>>     90, 101, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 83, 79, 85, 74, 88, 90, 101, 80, 80, 80, 80,
        >>> ]
        >>> extremeQuantOverLimit_values = [80] * 24 + [280] + extremeQuantOverLimit_values
        >>> extremeQuantOverLimit_times = np.add(time.time(), np.arange(len(extremeQuantOverLimit_values), 0, step=-1)*(-60)).tolist()
        >>> obj = AirCoolerSensorFailureDiagnosis()
        >>> for i in range(len(extremeQuantOverLimit_values)):
        >>>     print(
        >>>         obj.diagnosis(extremeQuantOverLimit_values[i], extremeQuantOverLimit_times[i])
        >>>     )

        [5]备注
        --------
        1.在定义peak2PeakOverLimitFault_truthTable时需注意,其小于阈值时应报警,其它情况正常
        2.truthTable的单个key长度要一致,且要等于key的数量
        3.truthTable的key的数量 = thresholds的长度 + 1
        """
        self.maximumTimeRange = kwargs["maximumTimeRange"] if "maximumTimeRange" in kwargs.keys() else 3600 * 24  # 秒
        self.minimumTimeRange = kwargs["minimumTimeRange"] if "minimumTimeRange" in kwargs.keys() else 600  # 秒
        self.neighboringPeakMinimumHeight = kwargs["neighboringPeakMinimumHeight"] if "neighboringPeakMinimumHeight" in kwargs.keys() else 2  # 相邻的两个极值点最小差值
        self.realtimeTemperThreshold = kwargs["realtimeTemperThreshold"] if "realtimeTemperThreshold" in kwargs.keys() else 205
        self.historyTemperDiffThreshold = kwargs[
            "historyTemperDiffThreshold"] if "historyTemperDiffThreshold" in kwargs.keys() else 0.2
        self.extremePointQuantThreshold = kwargs[
            "extremePointQuantThreshold"] if "extremePointQuantThreshold" in kwargs.keys() else 5

        self.truthTable = TruthTable()
        if "temperOverLimitFault_truthTable" in kwargs.keys():
            self.truthTable.temperOverLimitFault_truthTable = kwargs["temperOverLimitFault_truthTable"]
        if "peakQuantOverLimitFault_truthTable" in kwargs.keys():
            self.truthTable.peakQuantOverLimitFault_truthTable = kwargs["peakQuantOverLimitFault_truthTable"]
        if "peak2PeakOverLimitFault_truthTable" in kwargs.keys():
            self.truthTable.peak2PeakOverLimitFault_truthTable = kwargs["peak2PeakOverLimitFault_truthTable"]

        self.buffer = pd.DataFrame({"time": [], "value": []})  # 时间/温度缓存


    def __updateBuffer(self, newData: pd.DataFrame):
        # 新数据拼接
        self.buffer = pd.concat([self.buffer, newData])
        self.buffer = self.buffer.sort_values(["time"])
        # 有效时间筛选
        _nowTs = newData["time"].values.flatten().tolist()[-1]
        _validEarliestTime = _nowTs - self.maximumTimeRange
        self.buffer = self.buffer.where(self.buffer["time"] >= _validEarliestTime).dropna()
        self.buffer = self.buffer.reset_index(drop=True)

    def diagnosis(self, tempers: float, timestamp: float):
        """
        ①检查当前输入数据是否超过最大允许阈值

        ②检查短时间内合法极值点数量是否超限

        ③检查长时间内峰峰值是否未达到合理抖动阈值之上

        Parameters
        ----------
        tempers:
            float, 当前温度值(所有关联测点温度最大值)
        timestamp:
            float, 当前时间戳

        Returns
        -------

        """
        _cache = pd.DataFrame({"time": [timestamp], "value": [tempers]})
        self.__updateBuffer(_cache)
        # 检查是否有突破阈值的情况
        obj = MultipleThresholds_GreaterEqualTo_LesserThan(thresholds=[self.realtimeTemperThreshold],
                                                           truthTable=self.truthTable.temperOverLimitFault_truthTable)
        _res = obj.diagnosis(tempers)
        if len(_res["dfem_code"]) > 0:
            _res["dfem_evidence"] = [_res["dfem_evidence"]]
            _res["dfem_code"] = [_res["dfem_code"]]
            return _res
        else:
            _res = {"dfem_evidence": [], "dfem_code": []}
            # 极值点数量超限判断
            _bufferCache = self.buffer.where(self.buffer["time"] >= (timestamp - self.minimumTimeRange), np.nan).dropna()
            _bufferCache = _bufferCache.reset_index(drop=True)
            if len(_bufferCache) > 0:
                # 找极值点
                _extremeTimes, _extremePeaks = ExtremePointFinder(
                    _bufferCache["time"].values.flatten().tolist(),
                    _bufferCache["value"].values.flatten().tolist()
                )
                # 找准极值点
                _extremeTimesPotential, _extremePeaksPotential = PotentialExtremePointFinder(
                    _bufferCache["time"].values.flatten().tolist(),
                    _bufferCache["value"].values.flatten().tolist()
                )
                _extremeTimes, _extremePeaks = _extremeTimes + _extremeTimesPotential, _extremePeaks + _extremePeaksPotential
                _legalLocs = list(map(np.abs, np.diff(_extremePeaks)))
                _legalLocs = [0] + _legalLocs
                _overLimitLocs = np.where(np.asarray(_legalLocs) > self.neighboringPeakMinimumHeight)[0]
                obj = MultipleThresholds_GreaterEqualTo_LesserThan(thresholds=[self.extremePointQuantThreshold],
                                                                   truthTable=self.truthTable.peakQuantOverLimitFault_truthTable)
                _resCache = obj.diagnosis(len(_overLimitLocs))
                if len(_resCache["dfem_code"]) != 0:
                    _res["dfem_evidence"].append(_resCache["dfem_evidence"])
                    _res["dfem_code"].append(_resCache["dfem_code"])
            # 峰峰值过小判断
            _bufferCache = self.buffer.where(self.buffer["time"] >= (timestamp - self.maximumTimeRange), np.nan).dropna()
            obj = MultipleThresholds_GreaterEqualTo_LesserThan(thresholds=[self.historyTemperDiffThreshold],
                                                               truthTable=self.truthTable.peak2PeakOverLimitFault_truthTable)
            _resCache = obj.diagnosis(max(_bufferCache["value"]) - min(_bufferCache["value"]))
            if len(_resCache["dfem_code"]) != 0:
                _res["dfem_evidence"].append(_resCache["dfem_evidence"])
                _res["dfem_code"].append(_resCache["dfem_code"])
            return _res
