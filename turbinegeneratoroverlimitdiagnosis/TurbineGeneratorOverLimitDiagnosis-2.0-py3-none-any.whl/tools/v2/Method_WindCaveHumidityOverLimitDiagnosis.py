from .GenericMethods import *


class WindCaveHumidityOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        风洞内湿度超限判断

        :math:`T < 0.75, 风洞内湿度正常`
        :math:`T ≥ 0.75, 风洞内湿度超限`

        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.75]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[风洞内湿度]实测值(measured)正常,阈值threshold", "dfem_code": ""},
                    "01": {"dfem_evidence": "[风洞内湿度]实测值(measured)超限,阈值threshold", "dfem_code": "SP000160"},
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
        >>>     "10": {"dfem_evidence": "[风洞内湿度]实测值(measured)正常,阈值threshold", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[风洞内湿度]实测值(measured)超限,阈值threshold", "dfem_code": "SP000160"},
        >>> }
        >>> obj = WindCaveHumidityOverLimitDiagnosis([0.75], truthTable)
        >>> for item in [0.1, 0.7, 1, 2]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.75]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
             "10": {"dfem_evidence": "[风洞内湿度]实测值(measured)正常,阈值threshold", "dfem_code": ""},
             "01": {"dfem_evidence": "[风洞内湿度]实测值(measured)超限,阈值threshold", "dfem_code": "SP000160"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
