from .GenericMethods import *


class WhichCarbonBrushTemperOverLimitDiagnosis:
    def __init__(self, **kwargs):
        """
        第i号碳刷运行温度异常

        :math:`T < 0.2, 碳刷运行温度整体无异常`

        :math:`T ≥ 0.2, 第i号碳刷运行温度异常`

        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.2]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)正常,阈值threshold", "dfem_code": ""},
                    "01": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)异常,阈值threshold", "dfem_code": "SP0002(i))"},
                }
        roundingFormat:
            str, 数值精度格式,默认"%2.2f"

        [2] 方法
        ----------
        diagnosis:
            同时诊断正负极碳刷温度偏差超限情况,

        [3] 返回
        -------
        -/-:
            list[dict],超限判断结论列表

        [4] 示例1
        --------
        >>> truthTable = {
        >>>     "10": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)正常,阈值threshold", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)异常,阈值threshold", "dfem_code": "SP0002(i))"},
        >>> }
        >>> obj = WhichCarbonBrushTemperOverLimitDiagnosis([0.2], truthTable)
        >>> for item in range(3):
        >>>     print(obj.diagnosis(
        >>>         {"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(), "seq": np.arange(1, 33)},
        >>>         {"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(), "seq": np.arange(33, 65)})
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.2]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "10": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)正常,阈值threshold", "dfem_code": ""},
            "01": {"dfem_evidence": "[第(i)号碳刷温度]偏差(measured)异常,阈值threshold", "dfem_code": "SP0002(i))"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        self.obj = MultipleThresholds_GreaterEqualTo_LesserThan(**kwargs)


    @staticmethod
    def __diag(multiThresholdsGreaterEqualToLesserThan_obj, tempersDict):
        _avgTemper = np.average(tempersDict["tempers"])
        _tempersPositive_bias = [(item - _avgTemper) / _avgTemper for item in tempersDict["tempers"]]
        res = []
        for i, item in enumerate(_tempersPositive_bias):
            _res = multiThresholdsGreaterEqualToLesserThan_obj.diagnosis(item)  # dict
            _res["dfem_code"] = _res["dfem_code"].replace("(i)", '0' + str(tempersDict["seq"][i]) if tempersDict["seq"][i]<10 else str(tempersDict["seq"][i]))
            _res["dfem_evidence"] = _res["dfem_evidence"].replace("(i)", str(tempersDict["seq"][i]))
            res.append(_res)
        return res

    def diagnosis(self, posTempers: dict, negTempers: dict) -> list:
        """
        同时诊断正负极碳刷温度偏差超限情况,

        posTempers / negTempers形如:
            {
                "tempers": [100, 102, 103],  # 温度的列表

                "seq": [1, 2, 3]  # 碳刷的序号
            }

        返回形如:
            [
                {'dfem_evidence': '[第23号碳刷温度]偏差(-0.12)正常,阈值0.20', 'dfem_code': ''},

                {'dfem_evidence': '[第24号碳刷温度]偏差(0.36)超限,阈值0.20', 'dfem_code': 'SP000224)'}
            ]

        :param posTempers: 正极的碳刷温度,形如: {"tempers": [100, 102, 103], "seq": [1, 2, 3]}.
        :type posTempers: dict

        :param negTempers: 负极的碳刷温度
        :type negTempers: float

        :return: 诊断结论
        """
        return self.__diag(self.obj, posTempers) + self.__diag(self.obj, negTempers)

