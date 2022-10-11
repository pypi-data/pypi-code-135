import pandas as pd

from .GenericMethods import *


EPSILON = 10e-10

def _func(coldWater, hotWater, coldWind, hotWind):
    if (hotWind - hotWater) / (coldWind - coldWater) > 0:
        return 0.01 * ((hotWind + coldWater) - (coldWind + hotWater)) / (
                    np.log((hotWind - hotWater) / (coldWind - coldWater + EPSILON)) + EPSILON)
    else:
        return np.nan

class AirCoolerDegradedDegreeDiagnosis:
    def __init__(self, **kwargs):
        """
        空冷器冷却效果劣化程度判断

        [1] 参数
        ----------
        func:
            str,对数温差计算公式,默认为[(Thi+Tci)-(Tho+Tco)]/(In((Thi-Tco)/(Tho-Tci))),可以通过完整的匿名函数指定如"lambda x: x..."
        truthTable:
            dict,判断真值表,其中,"i"、"(i)"不可变,默认:
                {
                    "01": {"dfem_code": "SP00042i", "dfem_evidence": "[第(i)号空冷器]运行异常(measured),阈值threshold"},
                    "10": {"dfem_code": "", "dfem_evidence": "[空冷器]冷却效果劣化程度相似"}
                }
        threshold:
            float,偏差门限值,默认0.1

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
        >>> a1 = np.random.randn(10, 1) + 70
        >>> a2 = np.random.randn(10, 1) + 82
        >>> a3 = np.random.randn(10, 1) + 85
        >>> a4 = np.random.randn(10, 1) + 86
        >>> a = np.concatenate([a1, a2, a3, a4], axis=1)
        >>> obj = AirCoolerDegradedDegreeDiagnosis()
        >>> for i in range(1):
        >>>     print(
        >>>         obj.diagnosis(a)
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1

        3.注意,diagnosis的返回值形如
        {'dfem_code': ['', '', ..., 'dfem_evidence': ['[空冷器]冷却效果劣化程度相似', '[空冷器]冷却效果劣化程度相似', ...}
        """

        self.func = eval(kwargs["func"]) if "func" in kwargs.keys() else _func
        _truthTable = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "01": {"dfem_code": "SP00042i", "dfem_evidence": "[第(i)号空冷器]运行异常(measured),阈值threshold"},
            "10": {"dfem_code": "", "dfem_evidence": "[空冷器]冷却效果劣化程度相似"},
        }
        _threshold = kwargs["threshold"] if "threshold" in kwargs.keys() else 0.1
        self.diagnosisObj = MultipleThresholds_GreaterEqualTo_LesserThan([_threshold], _truthTable)


    def diagnosis(self, tempers: np.array):
        _tempers = pd.DataFrame(tempers, columns=["coldWater", "hotWater", "coldWind", "hotWind"])
        _tempers["temperDiff"] = _tempers.apply(lambda x: self.func(x["coldWater"], x["hotWater"], x["coldWind"], x["hotWind"]), axis=1)
        _tempers = _tempers.dropna()
        _temperDiffs = _tempers["temperDiff"].values.flatten().tolist()
        _res = []
        for i in range(len(_tempers)):
            _cache = self.diagnosisObj.diagnosis(_temperDiffs[i])
            if "(i)" in _cache["dfem_evidence"]:
                _cache["dfem_evidence"] = _cache["dfem_evidence"].replace("(i)", str(i+1))
                _cache["dfem_code"] = _cache["dfem_code"].replace("i", str(i+1))
            _res.append(_cache)
        return listingDict2DictingList(_res)
