import pandas as pd

df1 =  pd.read_csv("data/processed/processed.csv")
df2 = pd.read_csv("data/processed/processed.csv")
result = pd.merge(df1, df2, how = "inner", on = "id_str")

result.to_csv('data/processed/processed.csv', index = False)