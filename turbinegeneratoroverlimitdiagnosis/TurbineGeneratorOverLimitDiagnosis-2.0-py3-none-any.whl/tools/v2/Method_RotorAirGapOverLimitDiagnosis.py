from .GenericMethods import *


class RotorAirGapOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        转子气隙（不均匀度）超限判断

        :math:`T ≤ 0.04, 转子气隙运行值正常`

        :math:`T > 0.04, 转子气隙运行值异常`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[0.04]
        truthTable:
            dict,报警真值表,默认:
                {
                    "10": {"dfem_evidence": "[转子气隙]正常", "dfem_code": ""},
                    "01": {"dfem_evidence": "[转子气隙]运行值(measured)异常,阈值threshold", "dfem_code": "SP000091"},
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
        >>>     "10": {"dfem_evidence": "[转子气隙]正常", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[转子气隙]运行值(measured)异常,阈值threshold", "dfem_code": "SP000091"},
        >>> }
        >>> obj = RotorAirGapOverLimitDiagnosis([0.04], truthTable, roundingFormat="%2.2f")
        >>> for item in [0.1, 0.2, 0.03]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [0.04]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "10": {"dfem_evidence": "[转子气隙]正常", "dfem_code": ""},
            "01": {"dfem_evidence": "[转子气隙]运行值(measured)异常,阈值threshold", "dfem_code": "SP000091"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
