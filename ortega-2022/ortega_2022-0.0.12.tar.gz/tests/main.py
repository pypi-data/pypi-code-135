import pandas as pd
import ortega_2022 as ORTEGA

samplein = 10
bigdata = pd.read_csv('/Users/rongxiangsu/rongxiang_jupyter/_data/CHTS_interaction/GpsPoints_'+str(samplein)+'min.csv',sep=',', header=0)
bigdata = bigdata[(bigdata['pid']==298473101)|(bigdata['pid']==719939301)]
bigdata['time_local'] = pd.to_datetime(bigdata.time_local)

print(bigdata[['pid','time_local']].head())
print(bigdata.columns.values)

# data: pd.DataFrame,
# id1: int,
# id2: int,
# starttime: str,
# endtime: str,
# MAX_EL_TIMETHRESH: float = 1000000000000000,
# MINUTE_DELAY: float = 180,
# latitude_field: str = "Latitude",
# longitude_field: str = "Longitude",
# tiger_ID: str = "tid",
# timefield: str = "Time_LMT",
# position_identifier: str = "position",
# time_format: str = "%Y-%m-%d %H:%M:%S",
interaction1 = ORTEGA.ORTEGA(bigdata,
                      id1=298473101,
                      id2=719939301
                      )



