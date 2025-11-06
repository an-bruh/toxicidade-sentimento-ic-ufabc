import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('/data/processed/processed.csv')

#definir 0 ou 1 para maior que 0.7

columns_to_modify = ['INSULT', 'TOXICITY', 'IDENTITY_ATTACK', 'THREAT', 'PROFANITY', 'SEVERE_TOXICITY']

for col in columns_to_modify:
  df[col] = df[col].apply(lambda x: 1 if x > 0.7 else 0)

x = df[['anx','anger','sad']].to_numpy()
y = df['SEVERE_TOXICITY'].to_numpy()
x = sm.add_constant(x)
model = sm.Logit(y, x)
result = model.fit(method='newton',maxiter=15)
result.params
result.predict(x)
(result.predict(x) >= 0.5).astype(int)
result.pred_table()

result.summary()
saida = result.summary()
with open("/data/processed/processed.txt", "w") as text_file:
    text_file.write(str(saida))