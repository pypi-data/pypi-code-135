import pandas as pd
df = pd.read_csv('/data/jianping/bokey/OCAICM/dataset/TEN/TEN_pro.csv')
cols = list(df.columns)
cols.remove('Smiles')
# df = df.loc[[1,2,3],list(df.columns).remove('Smiles')]
print(list(df.columns))