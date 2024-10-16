from googleapiclient import discovery
import read_key


def request(mensagem, atributos):
  API_KEY = read_key.chave()

  client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
  )

  analyze_request = {
    'comment': { 'text': mensagem},
    'requestedAttributes': atributos,
    'languages': ['pt']
  }

  response = client.comments().analyze(body=analyze_request).execute()

  return response