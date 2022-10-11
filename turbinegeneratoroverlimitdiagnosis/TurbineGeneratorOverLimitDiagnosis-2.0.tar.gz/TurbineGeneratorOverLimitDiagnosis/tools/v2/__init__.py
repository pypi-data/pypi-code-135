"""
Classes
-------
1.StatorWindingTemperOverLimitDiagnosis:定子绕组温度超限评估

2.StatorBusRingTemperOverLimitDiagnosis:定子汇流环温度超限评估

3.StatorCoreTemperOverLimitDiagnosis:定子铁芯温度超限评估

4.StatorWindingInsulationOverLimitDiagnosis:定子绕组绝缘超限评估

5.StatorCoreVibrationOverLimitDiagnosis:定子铁芯振动超限评估

6.StatorWindingVibrationOverLimitDiagnosis:定子绕组振动超限评估

7.RotorTemperOverLimitDiagnosis:转子温度超限评估

8.RotorExcitingCurrentOverLimitDiagnosis:转子励磁电流实测值与预测值比率超限评估

9.RotorAirGapOverLimitDiagnosis:转子气隙（不均匀度）超限判断

10.UpperGuideBearingSwingOverLimitDiagnosis:上导轴承摆度超限评估

11.TurbineGuideBearingSwingOverLimitDiagnosis:水导轴承摆度超限评估

12.StatorFrameHorizontalVibrationOverLimitDiagnosis:定子机座水平振动超限评估

13.StatorUpperFrameHorizontalVibrationOverLimitDiagnosis:定子上机架水平振动超限评估

14.SupportCoverHorizontalVibrationOverLimitDiagnosis:支持盖水平振动超限评估

15.WindCaveDustDensityOverLimitDiagnosis:风洞内粉尘浓度超限判断

16.WindCaveHumidityOverLimitDiagnosis:风洞内湿度超限判断

17.WindCaveNoiseOverLimitDiagnosis:风洞内噪声水平超限判断

18.TurbineRoomNoiseOverLimitDiagnosis:水车室噪声水平超限判断

19.CarbonBrushTemperOverLimitDiagnosis:碳刷温度超限判断

20.WhichCarbonBrushTemperOverLimitDiagnosis:第i号碳刷运行温度异常判断

21.CollectorRingSparkDangerDiagnosis:集电环存在打火隐患评估

22.WhichCarbonBrushCurrentOverLimitDiagnosis:第i号碳刷负载电流异常判断

23.AirCoolerSensorFailureDiagnosis:通风冷却系统传感器故障判断

24.AirCoolerDegradedDegreeDiagnosis:空冷器冷却效果劣化程度判断

25.UpperGuideBearingPadTemperOverLimitDiagnosis:上导轴承瓦温超限判断

26.UpperGuideBearingOilTankTemperOverLimitDiagnosis:上导轴承油槽温度超限判断

27.UpperGuideBearingOilTankHumidityOverLimitDiagnosis:上导轴承油槽水分含量超限判断

28.UpperGuideBearingOilViscosityOverLimitDiagnosis:上导轴承油槽油黏度超限判断

29.UpperGuideBearingOilTankMetalContentOverLimitDiagnosis:上导轴承油槽金属颗粒含量超限判断

30.UpperGuideBearingOilTankMetalIncrementOverLimitDiagnosis:上导轴承油槽金属颗粒增加量超限判断

31.UpperGuideBearingOilCoolerDiagnosis:上导轴承油冷却器评估

32.UpperGuideBearingPadDegradedDegreeDiagnosis:上导轴承瓦瓦面劣化程度评估

33.WhichUpperGuideBearingPadAbnormalStressDiagnosis:第i号上导轴瓦受力异常评估

34.ThrustBearingPadTemperOverLimitDiagnosis:推力轴承瓦温超限判断

35.ThrustBearingOilTankTemperOverLimitDiagnosis:推力轴承油槽温度超限判断

36.ThrustBearingOilTankHumidityOverLimitDiagnosis:推力轴承油槽水分含量超限判断

37.ThrustBearingOilViscosityOverLimitDiagnosis:推力轴承油槽油黏度超限判断

38.ThrustBearingOilTankMetalContentOverLimitDiagnosis:推力轴承油槽金属颗粒含量超限判断

39.ThrustBearingOilTankMetalIncrementOverLimitDiagnosis:推力轴承油槽金属颗粒增加量超限判断

40.ThrustBearingOilCoolerDiagnosis:推力轴承油冷却器评估

41.ThrustBearingPadLubricationPerformanceDiagnosis:推力轴承瓦面润滑性能评估

42.ThrustBearingPadDegradedDegreeDiagnosis:推力轴承瓦瓦面劣化程度评估

43.WhichThrustBearingPadAbnormalStressDiagnosis:第i号推力轴瓦受力异常评估

GenericMethods
---------
1.TwoThresholdsGreaterEqualToAndLesserThan: 如 T<T_min, T_min<=T<T_max, T_max<T的判断,输出是判断结论与判据

2.OneThresholdLesserEqualToAndGreaterThan: 如 T<=T_0, T_0<T的判断,输出是判断结论与判据

3.MultipleThresholds_GreaterEqualTo_LesserThan: 如 不定{T_i}的判断,输出是判断(T_i ≤ T < T_i+1)结论与判据

4.noiseWeightedAverageDB_cal: 计算噪声计权平均声压级(噪声平均值)

5.listingDict2DictingList: list型dict转换成dict型list
"""

from . import *
