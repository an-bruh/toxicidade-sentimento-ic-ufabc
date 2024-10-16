import api_request
import pandas as pd
import time
import json

dicio = {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'IDENTITY_ATTACK': {}, 'INSULT': {}, 'PROFANITY': {}, 'THREAT': {}}

def converter(mensagem, atributos = dicio):

    response = api_request.request(mensagem, atributos)

    summary_scores = {key: value['summaryScore']['value'] for key, value in response['attributeScores'].items()}
    
    #response_json = json.dumps(response['attributeScores'], indent=2)
    
    #data = json.loads(response_json)

    # Extract summary scores
    
    #summary_scores = {key: value['summaryScore']['value'] for key, value in data.items()}

    #df = pd.DataFrame.from_dict(pd.json_normalize(summary_scores), orient='columns')

    #return df
    #return delta_t
    return summary_scores

#print(converter("eu odeio python"))