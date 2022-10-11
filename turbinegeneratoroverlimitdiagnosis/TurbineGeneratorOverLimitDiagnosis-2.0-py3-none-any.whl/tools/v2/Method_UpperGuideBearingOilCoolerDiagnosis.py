from .GenericMethods import *


EPSILON = 10e-10

def _func(inletWaterTemper, outletWaterTemper, coldOilTemper, hotOilTemper, Ql=9.5, Qw=0.35):
    Tco1 = hotOilTemper - 2.1 * Qw * (outletWaterTemper - inletWaterTemper) / Ql
    return (coldOilTemper - Tco1) / Tco1


class UpperGuideBearingOilCoolerDiagnosis:
    def __init__(self, **kwargs):
        """
        上导轴承油冷却器评估

        [1] 参数
        ----------
        func:
            str,冷油温度实测值与计算值偏差,默认为Tco1=Thi-2.1*Qw*（Two-Twi）/Ql,可以通过完整的函数进行定义.上导油冷却器进水温度Twi、出水温度Two、冷油温度Tco、热油温度Thi、冷却水流量Qw
        truthTable:
            dict,判断真值表,其中,"i"、"(i)"不可变,默认:
                {
                    "10": {"dfem_code": "", "dfem_evidence": "[上导轴承油冷却器]运行正常"},
                    "01": {"dfem_code": "SP000490", "dfem_evidence": "[上导轴承油冷却器]运行异常,冷油温度计算值偏差(measured),阈值threshold"},
                }
        threshold:
            float,偏差门限值,默认0.1

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
        >>> tempers = (np.multiply(np.random.randn(10, 4), np.asarray([1, 1, 100, 1]).transpose())+80)
        >>> obj = UpperGuideBearingOilCoolerDiagnosis()
        >>> for item in tempers:
        >>>     print(obj.diagnosis(*item))

        [5]备注
        --------
        1.truthTable的单个key长度要一致,且要等于key的数量

        2.truthTable的key的数量 = thresholds的长度 + 1

        """

        self.func = kwargs["func"] if "func" in kwargs.keys() else _func
        _truthTable = kwargs["truthTable"] if "truthTable" in kwargs.keys() else {
            "10": {"dfem_code": "", "dfem_evidence": "[上导轴承油冷却器]运行正常"},
            "01": {"dfem_code": "SP000490", "dfem_evidence": "[上导轴承油冷却器]运行异常,冷油温度计算值偏差(measured),阈值threshold"},
        }
        _threshold = kwargs["threshold"] if "threshold" in kwargs.keys() else 0.1
        self.diagnosisObj = MultipleThresholds_GreaterEqualTo_LesserThan([_threshold], _truthTable)


    def diagnosis(self, inletWaterTemper, outletWaterTemper, coldOilTemper, hotOilTemper):
        """
        评估

        调用该方法时,入参顺序需与self.func方法的入参顺序一致

        :param inletWaterTemper: 进水温度
        :type inletWaterTemper: float

        :param outletWaterTemper: 出水温度
        :type outletWaterTemper: float

        :param coldOilTemper: 冷油温度
        :type coldOilTemper: float

        :param hotOilTemper: 热油温度
        :type hotOilTemper: float
        :return: dict, 评估结果
        """
        return self.diagnosisObj.diagnosis(self.func(inletWaterTemper, outletWaterTemper, coldOilTemper, hotOilTemper))
