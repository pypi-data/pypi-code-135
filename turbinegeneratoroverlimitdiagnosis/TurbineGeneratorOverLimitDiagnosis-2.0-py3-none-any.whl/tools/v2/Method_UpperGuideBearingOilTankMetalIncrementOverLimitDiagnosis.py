from .GenericMethods import *


class UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        上导轴承油槽金属颗粒增加量超限判断

        :math:`T < 800, 上导轴承油槽金属颗粒增加量正常`

        :math:`T ≥ 800, 上导轴承油槽金属颗粒数量增加量超限`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[800]
        truthTable:
            dict,报警真值表,形如:{
            "10": {"dfem_evidence": "[上导轴承油槽金属颗粒数量增加量]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[上导轴承油槽金属颗粒数量增加量]实测值(measured)超限报警,阈值threshold", "dfem_code": "SP000470"},
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
        >>> tempers = (np.random.randn(10, 1)*0.1 + 800).flatten().tolist()
        >>> obj = UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis()
        >>> for i in tempers:
        >>>     print(
        >>>         obj.diagnosis(i)
        >>>     )

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        thresholds = [800]
        truthTable = {
            "10": {"dfem_evidence": "[上导轴承油槽金属颗粒数量增加量]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[上导轴承油槽金属颗粒数量增加量]实测值(measured)超限报警,阈值threshold", "dfem_code": "SP000480"},
        }
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else thresholds
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else truthTable
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
