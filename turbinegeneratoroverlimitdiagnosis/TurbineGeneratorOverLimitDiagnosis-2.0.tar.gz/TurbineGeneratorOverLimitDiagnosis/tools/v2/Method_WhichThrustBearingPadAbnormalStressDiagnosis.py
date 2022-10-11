from .GenericMethods import *


class WhichThrustBearingPadAbnormalStressDiagnosis:
    def __init__(self, **kwargs):
        """
        第i号推力轴瓦受力异常评估

        :math:`T < 0.035, 推力轴瓦受力无异常`

        :math:`T ≥ 0.035, 第i号推力轴瓦受力异常`

        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.035]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[第(i)号推力轴瓦受力]温度偏差计算值(measured)正常,阈值threshold", "dfem_code": ""},
                    "01": {"dfem_evidence": "[第(i)号推力轴瓦受力]温度偏差计算值(measured)异常,阈值threshold", "dfem_code": "SP0007(i))"},
                }
        roundingFormat:
            str, 数值精度格式,默认"%2.2f"

        [2] 方法
        ----------
        diagnosis:
            推力轴瓦温度与均值偏差超限情况

        [3] 返回
        -------
        -/-:
            list[dict],超限判断结论列表

        [4] 示例1
        --------
        >>> obj = WhichThrustBearingPadAbnormalStressDiagnosis()
        >>> for item in range(1):
        >>>     print(
        >>>         obj.diagnosis({"tempers": (np.multiply(np.abs(np.random.randn(32)), 115)).flatten().tolist(),
        >>>                        "seq": np.arange(1, 33)})
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.035]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "10": {"dfem_evidence": "[第(i)号推力轴瓦受力]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[第(i)号推力轴瓦受力]温度偏差计算值(measured)异常,阈值threshold", "dfem_code": "SP0007(i)"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        self.obj = MultipleThresholds_GreaterEqualTo_LesserThan(**kwargs)


    @staticmethod
    def __diag(multiThresholdsGreaterEqualToLesserThan_obj, tempersDict):
        _avgTemper = np.average(tempersDict["tempers"])
        _tempersPositive_bias = [abs((item - _avgTemper) / _avgTemper) for item in tempersDict["tempers"]]
        res = []
        for i, item in enumerate(_tempersPositive_bias):
            _res = multiThresholdsGreaterEqualToLesserThan_obj.diagnosis(item)  # dict
            _res["dfem_code"] = _res["dfem_code"].replace("(i)", '0' + str(tempersDict["seq"][i]) if tempersDict["seq"][i]<10 else str(tempersDict["seq"][i]))
            _res["dfem_evidence"] = _res["dfem_evidence"].replace("(i)", str(tempersDict["seq"][i]))
            res.append(_res)
        return res

    def diagnosis(self, tempers: dict) -> list:
        """
        轴瓦温度与均值偏差超限情况

        tempers形如:
            {
                "tempers": [100, 102, 103],  # 温度的列表

                "seq": [1, 2, 3]  # 轴瓦的序号
            }

        返回形如:
            {
                'dfem_evidence': [
                    '[第1号推力轴瓦受力]温度偏差计算值(1.39)异常,阈值0.04',
                    ...,
                    '[第3号推力轴瓦受力]温度偏差计算值(0.57)异常,阈值0.04'
                ],
                'dfem_code': [
                    'SP000701)',
                    ...,
                    'SP000702)'
                ]
            }


        :param tempers: 轴瓦温度,形如: {"tempers": [100, 102, 103], "seq": [1, 2, 3]}.
        :type posTempers: dict

        :return: 诊断结论
        """
        return listingDict2DictingList(self.__diag(self.obj, tempers))

