from .GenericMethods import *


class StatorCoreVibrationOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        定子铁芯振动超限判断,单位均为mm

        :math:`T ≤ 0.03, 定子铁芯振动不超限`
        :math:`T > 0.03, 定子铁芯振动超限报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.03]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[定子铁芯振动]正常", "dfem_code": ""},
                    "01": {"dfem_evidence": "[定子铁芯振动]实测值(measured)指标超限,阈值threshold", "dfem_code": "SP000051"},
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
        >>>     "10": {"dfem_evidence": "[定子铁芯振动]正常", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[定子铁芯振动]实测值(measured)指标超限,阈值threshold", "dfem_code": "SP000051"},
        >>> }
        >>> obj = StatorCoreVibrationOverLimitDiagnosis([0.03], truthTable, roundingFormat="%2.2f")
        >>> for item in [0.005, 0.07, 0.09, 0.0002]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.03]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "10": {"dfem_evidence": "[定子铁芯振动]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[定子铁芯振动]实测值(measured)指标超限,阈值threshold", "dfem_code": "SP000051"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
