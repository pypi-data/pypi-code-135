import numpy as np


class MultipleThresholds_GreaterEqualTo_LesserThan:
    def __init__(self, thresholds: list, truthTable: dict, roundingFormat: str="%2.2f"):
        """
        判断数值位于多个门限值的哪个区域(大于等于T_i且小于T_i+1)

        :math:`T < T_i`

        :math:`T_i ≤ T < T_i+1`

        :math:`T_2 ≤ T`

        真值表
        ------
        形如 {
            "1000X": {"dfem_code": "SP000001", "dfem_evidence": "[定子绕组运行温度]不超限"},

            "0100X": {"dfem_code": "SP000002", "dfem_evidence": "[定子绕组运行温度]实测值(measured)一级超限,阈值threshold"},

            "0010X": {"dfem_code": "SP000003", "dfem_evidence": "[定子绕组运行温度]实测值(measured)二级超限,阈值threshold"},

            "0001X": {"dfem_code": "SP000004", "dfem_evidence": "[定子绕组运行温度]实测值(measured)三级超限,阈值threshold"},

            "0001X": {"dfem_code": "SP000005", "dfem_evidence": "[定子绕组运行温度]实测值(measured)三级超限,阈值threshold"}

            "0001X": ...
        }

        其中“100”表示针对上式的判断结果,"measured"字符串会被替换成报警值(%2.2f),"threshold"字符串会被替换成报警阈值(%2.2f)

        :param thresholds: 阈值
        :param truthTable: 真值表
        :param roundingFormat: 数值精度格式,默认"%2.2f"
        """
        self.thresholds = np.asarray(thresholds)
        self.truthTable = truthTable
        self.roundingFormat = roundingFormat
        self.__legalityCheck()

    def __legalityCheck(self):
        """
        输入参数合法性检查,
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        __keyLengths = np.unique(list(map(len, self.truthTable.keys())))
        __law_1 = (len(__keyLengths)==1) and (__keyLengths[0]==len(self.truthTable.keys()))
        __law_2 = len(self.truthTable.keys()) == len(self.thresholds) + 1
        if not __law_1:
            raise ValueError(f"truthTable的单个key长度({__keyLengths})要一致,且要等于key的数量({len(self.truthTable.keys())})")
        if not __law_2:
            raise ValueError(f"truthTable的key的数量({len(self.truthTable.keys())}) = thresholds的长度({len(self.thresholds)}) + 1")

    def diagnosis(self, x):
        _minimumLoc = np.where(x<self.thresholds)[0]
        minimumLoc = -1 if len(_minimumLoc) == 0 else _minimumLoc[0]
        _truthList = [0]*(len(self.thresholds)+1)
        _truthList[minimumLoc] = 1
        _truthStr = "".join(list(map(str, _truthList)))
        evidence = self.truthTable[_truthStr]["dfem_evidence"]\
            .replace("measured", str(f"{f'{self.roundingFormat}'%x}"))\
            .replace("threshold",
            str(f"{f'{self.roundingFormat}'%(self.thresholds[minimumLoc-1 if minimumLoc!=-1 else minimumLoc])}")
        )
        code = self.truthTable[_truthStr]["dfem_code"]
        return {"dfem_evidence": evidence, "dfem_code": code, }


class TwoThresholdsGreaterEqualToAndLesserThan:
    def __init__(self, lowerThreshold, higherThreshold, truthTable):
        """
        计算针对下式的判断结果

        :math:`T < T_lowerThreshold`

        :math:`T_lowerThreshold ≤ T < T_higherThreshold`

        :math:`T_higherThreshold ≤ T`

        真值表
        ------
        形如 {
            "100": "[定子绕组运行温度]不超限",

            "010": "[定子绕组运行温度]实测值(measured)一级超限,阈值threshold",

            "001": "[定子绕组运行温度]实测值(measured)二级超限,阈值threshold"
        }

        其中“100”表示针对上式的判断结果,"measured"字符串会被替换成报警值(%2.2f),"threshold"字符串会被替换成报警阈值(%2.2f)

        :param lowerThreshold: 判断高限
        :param higherThreshold: 判断高限
        :param truthTable: 真值表
        """
        self.lowerThreshold, self.higherThreshold = lowerThreshold, higherThreshold
        self.truthTable = truthTable

        def greaterEqualTo(x, x0):
            return x >= x0

        def lesserThan(x, x0):
            return x < x0

        self.diagDict = {
            "greaterEqualTo": greaterEqualTo,
            "lesserThan": lesserThan
        }


    def diagnosis(self, x):
        res =  [
            self.diagDict["lesserThan"](x, self.lowerThreshold),
            all([not self.diagDict["lesserThan"](x, self.lowerThreshold), not self.diagDict["greaterEqualTo"](x, self.higherThreshold)]),
            self.diagDict["greaterEqualTo"](x, self.higherThreshold)
        ]
        _eventDescribe = f"{self.truthTable[''.join(list(map(lambda x: str(int(x)), res)))]}"
        _threshold = np.asarray([np.nan, self.lowerThreshold, self.higherThreshold])[res]
        evidence = _eventDescribe.replace("measured", str(f"{'%2.2f'%x}")).replace("threshold", str(f"{'%2.2f'%(_threshold)}"))
        return evidence


class OneThresholdLesserEqualToAndGreaterThan:
    def __init__(self, threshold, truthTable):
        """
        计算针对下式的判断结果

        :math:`T \\le T_threshold

        :math:`T > T_threshold

        真值表
        ------
        形如 {
            "10": "定子绕组运行温度不超限",

            "01": "定子绕组运行温度超限一级报警",
        }

        其中“10”表示针对上式的判断结果

        :param threshold: 判断阈值
        :param truthTable: 真值表
        """
        self.threshold = threshold
        self.truthTable = truthTable

        def greaterThan(x, x0):
            return x > x0

        def lesserEqualTo(x, x0):
            return x <= x0

        self.diagDict = {
            "lesserEqualTo": lesserEqualTo,
            "greaterThan": greaterThan
        }


    def diagnosis(self, x):
        res =  [self.diagDict["lesserEqualTo"](x, self.threshold), self.diagDict["greaterThan"](x, self.threshold)]
        return self.truthTable["".join(list(map(lambda x: str(int(x)), res)))]


def noiseWeightedAverageDB_cal(*args, **kwargs) -> int:
    """
    计算噪声计权平均声压级(噪声平均值)

    :param args: 噪声数据,形如: (10, 20)
    :type args: tuple
    :param kwargs: 修正值、环境反射修正值,形如: {"Klis": [1, 2], "K2": 3}
    :type kwargs: dict
    :return: Lp 噪声计权平均声压级(噪声平均值)
    """
    N = len(args)
    Klis = kwargs["Klis"]  # list
    K2 = kwargs["K2"]  # float
    _epsilonElement = lambda LpAi, Kli: 10**(0.1*(LpAi - Kli))  # 10^(0.1*LpAi - Kli)
    _log = lambda x, N: np.log10(sum(x) / N)  # lg(sum(_epsilonElement)/N)
    _Lp = 10 * _log([_epsilonElement(item[0], item[1]) for item in zip(args, Klis)], N) - K2
    return _Lp


def listingDict2DictingList(listIn: list):
    """
    list型dict转换成dict型list,即[dict, dict] --> dict[list],比如:

    a = [
        {key: "key1", value: "value1"},
        {key: "key2", value: "value2"}
    ]

    b = {
        key: ["key1", "key2"], value: ["value1", "value2"]
    }

    更新数据样本，并判断当前数据近期的变化状态

    :param listIn: 元素为具有相同key的多个dict型变量
    :type listIn: list

    :return: key和value中的变量是list型的多个元素
    """
    keys = listIn[0].keys()
    res = {}
    for item in keys:
        _res = {item: [jtem[item] for jtem in listIn]}
        res = {**res, **_res}
    return res