from .GenericMethods import *


class ThrustBearingOilTankHumidityOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        推力轴承油槽水分含量超限判断

        :math:`T < 0.015, 推力轴承油槽水分含量不超限`

        :math:`T ≥ 0.015, 推力轴承油槽水分含量超限报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.015]
        truthTable:
            dict,报警真值表,形如:{
            "10": {"dfem_evidence": "[推力轴承油槽水分含量]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[推力轴承油槽水分含量]实测值(measured)超限报警,阈值threshold", "dfem_code": "SP000540"},
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
        >>> tempers = (np.random.randn(5, 1)*0.1 + 0.015).flatten().tolist() + (np.random.randn(5, 1)*0.1 + 0.015).flatten().tolist()
        >>> obj = ThrustBearingOilTankHumidityOverLimitDiagnosis()
        >>> for i in tempers:
        >>>     print(
        >>>         obj.diagnosis(i)
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        thresholds = [0.015]
        truthTable = {
            "10": {"dfem_evidence": "[推力轴承油槽水分含量]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[推力轴承油槽水分含量]实测值(measured)超限报警,阈值threshold", "dfem_code": "SP000540"},
        }
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else thresholds
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else truthTable
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
