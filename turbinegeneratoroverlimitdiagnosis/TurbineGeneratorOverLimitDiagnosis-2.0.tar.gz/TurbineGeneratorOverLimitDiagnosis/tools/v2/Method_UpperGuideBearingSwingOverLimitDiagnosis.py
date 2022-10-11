from .GenericMethods import *


class UpperGuideBearingSwingOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        上导摆度运行值超限判断,单位均为mm

        :math:`T < 0.15, 上导摆度运行值不超限`

        :math:`0.15 ≤ T < 0.20, 上导摆度运行值超限一级报警`

        :math:`T ≥ 0.20, 上导摆度运行值超限二级报警`


        [1] 参数
        ----------
        thresholds:
            list[float],一级报警限,默认[0.15, 0.2]
        truthTable:
            dict,报警真值表,形如:
                {
                    "100": {"dfem_evidence": "[上导摆度]正常", "dfem_code": ""},
                    "010": {"dfem_evidence": "[上导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000101"},
                    "001": {"dfem_evidence": "[上导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000102"},
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
        >>>     "100": {"dfem_evidence": "[上导摆度]正常", "dfem_code": ""},
        >>>     "010": {"dfem_evidence": "[上导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000101"},
        >>>     "001": {"dfem_evidence": "[上导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000102"},
        >>> }
        >>> obj = UpperGuideBearingSwingOverLimitDiagnosis([0.15, 0.2], truthTable, roundingFormat="%2.2f")
        >>> for item in [0.1, 0.18, 0.3]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1

        3.报警次数计数在本模块外部进行
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.15, 0.2]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "100": {"dfem_evidence": "[上导摆度]正常", "dfem_code": ""},
            "010": {"dfem_evidence": "[上导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000101"},
            "001": {"dfem_evidence": "[上导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000102"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
