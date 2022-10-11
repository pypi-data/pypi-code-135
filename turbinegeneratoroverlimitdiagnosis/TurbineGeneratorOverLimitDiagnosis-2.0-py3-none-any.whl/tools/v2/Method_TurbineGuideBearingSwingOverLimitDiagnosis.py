from .GenericMethods import *


class TurbineGuideBearingSwingOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        水导摆度运行值超限判断,单位均为mm

        :math:`T < 0.18, 水导摆度运行值不超限`

        :math:`0.18 ≤ T < 0.23, 水导摆度运行值超限一级报警`

        :math:`T ≥ 0.23, 水导摆度运行值超限二级报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.18, 0.23]
        truthTable:
            dict,报警真值表,形如:
                {
                    "100": {"dfem_evidence": "[水导摆度]正常", "dfem_code": ""},
                    "010": {"dfem_evidence": "[水导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000111"},
                    "001": {"dfem_evidence": "[水导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000112"},
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
        >>>     "100": {"dfem_evidence": "[水导摆度]正常", "dfem_code": ""},
        >>>     "010": {"dfem_evidence": "[水导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000111"},
        >>>     "001": {"dfem_evidence": "[水导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000112"},
        >>> }
        >>> obj = TurbineGuideBearingSwingOverLimitDiagnosis([0.18, 0.23], truthTable, roundingFormat="%2.2f")
        >>> for item in [0.1, 0.18, 0.3]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.18, 0.23]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "100": {"dfem_evidence": "[水导摆度]正常", "dfem_code": ""},
            "010": {"dfem_evidence": "[水导摆度]运行值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000111"},
            "001": {"dfem_evidence": "[水导摆度]运行值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000112"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
