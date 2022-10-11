from .GenericMethods import *


class WindCaveNoiseOverLimitDiagnosis:
    def __init__(self, noises, Klis, K2, **kwargs):
        """
        风洞内噪声水平异常判断

        :math:`T < 85, 风洞内噪声水平正常`

        :math:`T ≥ 85, 风洞内噪声水平异常`

        [1] 参数
        ----------
        noises:
            tuple,噪声值
        Klis:
            list[float],背景噪声修正值
        K2:
            float,环境反射修正值
        thresholds:
            list[float],报警限,默认[85]
        truthTable:
            dict,报警真值表,形如:
                {
                    "10": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)正常,阈值threshold", "dfem_code": ""},
                    "01": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)超限,阈值threshold", "dfem_code": "SP000170"},
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
        >>>     "10": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)正常,阈值threshold", "dfem_code": ""},
        >>>     "01": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)超限,阈值threshold", "dfem_code": "SP000170"},
        >>> }
        >>> for item in [(1, 2), (11, 12), (21, 22), (60, 80), (100, 90)]:
        >>>     obj = WindCaveNoiseOverLimitDiagnosis(item, Klis=[4, 4], K2=4, thresholds=[85], truthTable=truthTable)
        >>>     print(obj.diagnosis())

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量
        2.truthTable的key的数量 = thresholds的长度 + 1
        """

        self.thresholds = kwargs["thresholds"] if "thresholds" in kwargs.keys() else [85]
        self.truthTable = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
                    "10": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)正常,阈值threshold", "dfem_code": ""},
                    "01": {"dfem_evidence": "[风洞内噪声水平]实测值(measured)超限,阈值threshold", "dfem_code": "SP000170"},
                }
        self.roundingFormat = kwargs["roundingFormat"] if "roundingFormat" in kwargs.keys() else "%2.2f"
        self._Lp = noiseWeightedAverageDB_cal(*noises, Klis=Klis, K2=K2)

    def diagnosis(self):
        obj = MultipleThresholds_GreaterEqualTo_LesserThan(self.thresholds, self.truthTable, self.roundingFormat)
        return obj.diagnosis(self._Lp)
