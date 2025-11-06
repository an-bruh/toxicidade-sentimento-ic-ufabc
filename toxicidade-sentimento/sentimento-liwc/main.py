import pandas as pd
from nrclex import NRCLex
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')

text_object = NRCLex(lexicon_file='toxicidade-sentimento/sentimento-liwc/lexicon_portugues.json')

#list_emotions = []

df_og = pd.read_csv("data/processed/processed.csv")
df_og['anger'] = 0
df_og['anticipation'] = 0
df_og['disgust'] = 0
df_og['fear'] = 0
df_og['joy'] = 0
df_og['negative'] = 0
df_og['positive'] = 0
df_og['sadness'] = 0
df_og['surprise'] = 0
df_og['trust'] = 0

def emocoes(texto):
    emotions = text_object.load_raw_text(texto)
    emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']
    scores = {emotion: text_object.raw_emotion_scores.get(emotion, 0) for emotion in emotions}


    return scores
count = 1
for index, row in df_og.iterrows():
        print(f'Linha:{count}\n\n')
        #id = row['id_str']
        if isinstance(row['text'], str):
            emocoes_texto = emocoes(row['text'])
        else:
            emocoes_texto = emocoes('null') 
        #df_og.loc[index, ''] =   
        df_og.loc[index,'anger'] = emocoes_texto['anger']
        df_og.loc[index,'anticipation'] = emocoes_texto['anticipation']
        df_og.loc[index,'disgust'] = emocoes_texto['disgust']
        df_og.loc[index,'fear'] = emocoes_texto['fear']
        df_og.loc[index,'joy'] = emocoes_texto['joy']
        df_og.loc[index,'negative'] = emocoes_texto['negative']
        df_og.loc[index,'positive'] = emocoes_texto['positive']
        df_og.loc[index,'sadness'] = emocoes_texto['sadness']
        df_og.loc[index,'surprise'] = emocoes_texto['surprise']
        df_og.loc[index,'trust'] = emocoes_texto['trust']
        #emocoes_texto.update({'id_str': id})
        #list_emotions.append(emocoes_texto)
        count += 1
#df = pd.DataFrame(list_emotions)
df_og.to_csv('data/processed/processed.csv', index = False)