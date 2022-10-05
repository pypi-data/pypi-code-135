import pandas as pd
from sttm_groups import SttmGroups

df = pd.read_csv("../twitter_lib_tweetreply.csv")
df2 = df[:2001]
sttm = SttmGroups(df2, 'tw', comments=True)
df_test = sttm.get_sttm_groups()
print(df_test['sttm_group'].value_counts())