import pandas as pd
from src.dataframetranslationscoring.scoring import translation_quantitative_scoring

df_original = pd.read_excel("./tests/SAIB_TablesNames_Translated.xlsx")
df_translated = df_original[["Microsoft translation"]]
df_original = df_original[["Portuguese table name"]]
df_translated.rename(
    columns={"Microsoft translation": "Portuguese table name"}, inplace=True
)
df_original = df_original[:5]
df_translated = df_translated[:5]
print(translation_quantitative_scoring(df_original, df_translated))
