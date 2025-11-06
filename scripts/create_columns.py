import pandas as pd

dictio = {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'IDENTITY_ATTACK': {}, 'INSULT': {}, 'PROFANITY': {}, 'THREAT': {}}

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

df = pd.read_csv('data/cleaned/clean.csv')
df = create_columns(df, dictio)

df.to_csv('data/cleaned/clean.csv', index=False)
