# from TurbineGeneratorOverLimitDiagnosis.tools.v2.Method_WaterGuideBearingSwingOverLimitDiagnosis import WaterGuideBearingSwingOverLimitDiagnosis
from tools.v2.Method_TurbineGuideBearingSwingOverLimitDiagnosis import TurbineGuideBearingSwingOverLimitDiagnosis


def main():
    obj = TurbineGuideBearingSwingOverLimitDiagnosis(roundingFormat="%2.2f")
    for item in [0.1, 0.18, 0.3]:
        print(obj.diagnosis(item))


if __name__ == '__main__':
    main()
