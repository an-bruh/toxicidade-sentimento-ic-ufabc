from googleapiclient import discovery
import pandas as pd
import time
import os
from datetime import datetime
print('Hora de inicio:')
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

data_origin = 'dados/raw/data.csv'
data_destiny = 'dados/processed/data_processed.csv'

dictio = {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'IDENTITY_ATTACK': {}, 'INSULT': {}, 'PROFANITY': {}, 'THREAT': {}}

def get_chave():
  keyFromFile = open("key/key_file")

  key = keyFromFile.read()
  keyFromFile.close()

  return key

def client_build(chave):
  API_KEY = chave

  client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey= API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
  )

  return client

def request(client, mensagem, atributos = dictio):

  analyze_request = {
    'comment': { 'text': mensagem},
    'requestedAttributes': atributos,
    'languages': ['pt'],
    'doNotStore': True
  }

  response = client.comments().analyze(body=analyze_request).execute()

  return response

def converter(response):

    summary_scores = {key: value['summaryScore']['value'] for key, value in response['attributeScores'].items()}

    return summary_scores

chave = get_chave()

cliente = client_build(chave)

df = pd.read_csv(data_origin)

try:
    for index, row in df.iterrows():
      if row['processed'] == False:
        resposta = request(cliente, row['full_text'])
        summaries = converter(resposta)
        for key, value in summaries.items():
            df.at[index, key] = value
        time.sleep(0.110)
        df.at[index,'processed'] = True
        if (index + 1) % 2000 == 0:
          print(f'\nSalvo no index: {index}')
          df.to_csv(data_destiny, index = False)
except Exception as e:
    # Garante que o diretório 'logs' exista
    os.makedirs("logs", exist_ok=True)

    log_path = "logs/log_error.log"

    # Abre o arquivo de log em modo append para não sobrescrever os anteriores
    with open(log_path, "a") as log_file:
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      log_msg = (
          f"\n---\n"
          f"Data/hora: {timestamp}\n"
          f"Erro: {repr(e)}\n"
          #f"Ocorreu na linha: {count}\n"
      )
      log_file.write(log_msg)
    print(f"\nErro registrado no log: {log_path}")

df.to_csv(data_destiny, index = False)
print('\nHora de finalizacao:')
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))