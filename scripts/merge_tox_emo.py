import pandas as pd

dictio = {'anx': {}, 'anger': {}, 'sad': {}}

df_tox = pd.read_csv("/data/processed/processed.csv")
df_emo = pd.read_csv("/data/processed/processed.csv")

def create_columns(df, dictio):
  for column in dictio.keys():
    if not (column in df):
      print(f"\n{column} adicionada!")
      df[column] = 0.0
    else:
      print(f"\n{column} existe!")
  if not ('processed' in df):
    df['processed'] = False
  return df



df_final = create_columns(df_tox, dictio)


for index, row in df_tox.iterrows():
  df_final.at[index,'anx'] = df_emo.at[index,'anx']
  df_final.at[index,'anger'] = df_emo.at[index,'anger']
  df_final.at[index,'sad'] = df_emo.at[index,'sad']

df_final.to_csv("/data/processed/processed.csv", index=False)