from .GenericMethods import *


class StatorWindingTemperOverLimitDiagnosis(MultipleThresholds_GreaterEqualTo_LesserThan):
    def __init__(self, *args, **kwargs):
        """
        定子绕组温度超限判断,单位均为℃

        :math:`T < 110, 定子绕组运行温度不超限`

        :math:`110 ≤ T < 125, 定子绕组运行温度超限一级报警`

        :math:`125 ≤ T, 定子绕组运行温度超限二级报警`


        [1] 参数
        ----------
        thresholds:
            list[float],报警限,默认[110, 125]
        truthTable:
            dict,报警真值表,形如:
                {
                    "100": {"dfem_evidence": "[定子绕组运行温度]不超限", "dfem_code": ""},
                    "010": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)一级超限,阈值threshold", "dfem_code": "SP000001"},
                    "001": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)二级超限,阈值threshold", "dfem_code": "SP000002"},
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
        >>>     "100": {"dfem_evidence": "[定子绕组运行温度]不超限", "dfem_code": ""},
        >>>     "010": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)一级超限,阈值threshold", "dfem_code": "SP000001"},
        >>>     "001": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)二级超限,阈值threshold", "dfem_code": "SP000002"},
        >>> }
        >>> obj = StatorWindingTemperOverLimitDiagnosis([110, 125], truthTable)
        >>> for item in [90, 100, 113, 123, 133]:
        >>>     print(obj.diagnosis(item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1

        """
        kwargs["thresholds"] = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [110, 125]
        kwargs["truthTable"] = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "100": {"dfem_evidence": "[定子绕组运行温度]不超限", "dfem_code": ""},
            "010": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)一级超限,阈值threshold", "dfem_code": "SP000001"},
            "001": {"dfem_evidence": "[定子绕组运行温度]实测值(measured)二级超限,阈值threshold", "dfem_code": "SP000002"},
        }
        kwargs["roundingFormat"] = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        super().__init__(*args, **kwargs)
