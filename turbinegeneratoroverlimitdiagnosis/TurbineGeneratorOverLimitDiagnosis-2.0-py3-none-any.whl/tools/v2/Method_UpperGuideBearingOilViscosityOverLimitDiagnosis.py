from .GenericMethods import *


class UpperGuideBearingOilViscosityOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        上导轴承油槽油黏度超限判断

        :math:`T < 43.7, 上导轴承油槽油黏度超低限报警`

        :math:`T ≥ 43.7, 上导轴承油槽油黏度指标正常`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[43.7]
        truthTable:
            dict,报警真值表,形如:{
            "10": {"dfem_evidence": "[上导轴承油槽油黏度]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[上导轴承油槽油黏度]实测值(measured)超低限报警,阈值threshold", "dfem_code": "SP000460"},
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
        >>> tempers = (np.random.randn(10, 1)*0.1 + 43.7).flatten().tolist()
        >>> obj = UpperGuideBearingOilViscosityOverLimitDiagnosis()
        >>> for i in tempers:
        >>>     print(
        >>>         obj.diagnosis(i)
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        3.注意超低限报警的真值表key
        """
        thresholds = [43.7]
        truthTable = {
            "10": {"dfem_evidence": "[上导轴承油槽油黏度]实测值(measured)超低限报警,阈值threshold", "dfem_code": "SP000460"},
            "01": {"dfem_evidence": "[上导轴承油槽油黏度]正常", "dfem_code": ""},
        }
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else thresholds
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else truthTable
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
