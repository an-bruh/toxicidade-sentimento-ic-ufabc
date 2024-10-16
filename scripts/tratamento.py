import pandas as pd
#import sys
#sys.path.insert(0, '../toxicidade-sentimento/scripts')
import response_to_dataframe as rd
import time

t0 = time.time()

arquivo = open("dados/raw/mensagem100.txt")
mensagem = arquivo.read()
arquivo.close()

conj = set(mensagem.splitlines())

summary_list = list()
df = pd.DataFrame()

for data in conj:
    result = rd.converter(data)
    summary_list.append(result)

df = pd.DataFrame(summary_list)

t = time.time()
delta = t - t0


print(df)
print(delta)