from .GenericMethods import *


class SupportCoverHorizontalViberOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        支持盖水平振动超限判断,单位均为mm

        :math:`T < 0.07, 支持盖水平振动不超限`

        :math:`0.07 ≤ T < 0.09, 支持盖水平振动超限一级报警`

        :math:`T ≥ 0.09, 支持盖水平振动超限二级报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.07, 0.09]
        truthTable:
            dict,报警真值表,默认:
                {
                    "100": {"dfem_evidence": "[支持盖振动]正常", "dfem_code": ""},
                    "010": {"dfem_evidence": "[支持盖振动]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000141"},
                    "001": {"dfem_evidence": "[支持盖振动]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000142"},
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
        >>> truthTable = {
        >>>     "100": {"dfem_evidence": "[支持盖振动]正常", "dfem_code": ""},
        >>>     "010": {"dfem_evidence": "[支持盖振动]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000141"},
        >>>     "001": {"dfem_evidence": "[支持盖振动]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000142"},
        >>> }
        >>> obj = SupportCoverHorizontalViberOverLimitDiagnosis([0.07, 0.09], truthTable, roundingFormat="%2.2f")
        >>> for item in [0.01, 0.075, 0.085, 0.095]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.07, 0.09]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "100": {"dfem_evidence": "[支持盖振动]正常", "dfem_code": ""},
            "010": {"dfem_evidence": "[支持盖振动]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000141"},
            "001": {"dfem_evidence": "[支持盖振动]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000142"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
