from .GenericMethods import *


class StatorWindingInsulationOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        定子绕组绝缘超限判断

        :math:`T < 0.6, 定子绕组绝缘超限二级报警`
        :math:`0.6 ≤ T < 0.8, 定子绕组绝缘超限一级报警`
        :math:`T ≥ 0.8, 定子绕组绝缘不超限`

        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.6, 0.8]
        truthTable:
            dict,报警真值表,形如:
                {
                    "100": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)二级报警,阈值threshold", "dfem_code": "SP000042"},
                    "010": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)一级报警,阈值threshold", "dfem_code": "SP000041"},
                    "001": {"dfem_evidence": "[定子绕组绝缘劣化]不超限", "dfem_code": ""},
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
        >>>     "100": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)二级报警,阈值threshold", "dfem_code": "SP000042"},
        >>>     "010": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)一级报警,阈值threshold", "dfem_code": "SP000041"},
        >>>     "001": {"dfem_evidence": "[定子绕组绝缘劣化]不超限", "dfem_code": ""},
        >>> }
        >>> obj = StatorWindingInsulationOverLimitDiagnosis([0.6, 0.8], truthTable)
        >>> for item in [0.5, 0.7, 0.9, 2]:
        >>>     print(obj.diagnosis(item))


        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.6, 0.8]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "100": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)二级报警,阈值threshold", "dfem_code": "SP000042"},
            "010": {"dfem_evidence": "[定子绕组绝缘劣化]实测值(measured)一级报警,阈值threshold", "dfem_code": "SP000041"},
            "001": {"dfem_evidence": "[定子绕组绝缘劣化]不超限", "dfem_code": ""},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
