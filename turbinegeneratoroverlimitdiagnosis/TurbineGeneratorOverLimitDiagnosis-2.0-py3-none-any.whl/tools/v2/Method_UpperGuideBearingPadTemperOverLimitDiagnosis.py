from .GenericMethods import *


class UpperGuideBearingPadTemperOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        上导轴承瓦温超限判断

        :math:`T < 75, 上导轴承瓦温不超限`

        :math:`75 ≤ T < 85, 上导轴承瓦温超限一级报警`

        :math:`T ≥ 85, 上导轴承瓦温超限二级报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[75, 85]
        truthTable:
            dict,报警真值表,形如:
                {
                    "100": {"dfem_evidence": "[上导轴承瓦温]正常", "dfem_code": ""},
                    "010": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000431"},
                    "001": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000432"},
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
        >>> tempers = (np.random.randn(5, 1) + 75).flatten().tolist() + (np.random.randn(5, 1) + 85).flatten().tolist()
        >>> thresholds = [75, 85]
        >>> truthTable = {
        >>>     "100": {"dfem_evidence": "[上导轴承瓦温]正常", "dfem_code": ""},
        >>>     "010": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000431"},
        >>>     "001": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000432"},
        >>> }
        >>> obj = UpperGuideBearingPadTemperOverLimitDiagnosis(thresholds=thresholds, truthTable=truthTable)
        >>> for i in tempers:
        >>>     print(
        >>>         obj.diagnosis(i)
        >>>     )


        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """
        thresholds = [75, 85]
        truthTable = {
            "100": {"dfem_evidence": "[上导轴承瓦温]正常", "dfem_code": ""},
            "010": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限一级报警,阈值threshold", "dfem_code": "SP000431"},
            "001": {"dfem_evidence": "[上导轴承瓦温]实测值(measured)超限二级报警,阈值threshold", "dfem_code": "SP000432"},
        }
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else thresholds
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else truthTable
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
