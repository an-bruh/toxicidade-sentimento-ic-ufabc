import spacy
import pandas as pd
from spacy.lang.pt.stop_words import STOP_WORDS
import unicodedata

df_og = pd.read_csv("data/processed/processed.csv")

# Carrega o modelo spaCy para português
nlp = spacy.load('pt_core_news_sm')

# Lista de palavras que não devem ser convertidas para masculino
# Essa lista inicial é meio arbitrária. De início, contem: palavras
# femininas sem equivalente masculino (como "praça"); palavras
# masculinas que violam as heuristicas (poeta).
# Uma palavra deve ser acrescentada aqui caso:
# - a palavra aparece no dicionário de sentimentos na forma feminina
# - caso convertida pelas heuristicas, o resultado gera um erro
# de interpretação, por exemplo bola -> bolo
nao_converter = [
    "praça", "bola", "rua", "janela", "porta", "mesa", "alma", "pena",
    "fome", "sede", "vítima", "espécie", "criança", "pessoa", "testemunha",
    "poeta", "profeta", "clima", "vergonha",
]

# Lista de exceções irregulares (feminino => masculino)
excecoes = {
    "atriz": "ator",
    "deusa": "deus",
    "heroína": "herói",
    "profetisa": "profeta",
    "poetisa": "poeta",
    "sacerdotisa": "sacerdote",
    "princesa": "príncipe",
    "duquesa": "duque",
    "condessa": "conde",
    "imperatriz": "imperador",
}

# Verifica se uma palavra existe no vocabulário do spaCy
def palavra_existe(palavra):
    return palavra in nlp.vocab and nlp.vocab[palavra].is_alpha

# Converte feminino para masculino com base em regras e exceções
def feminino_para_masculino(palavra):
    if palavra in excecoes:
        return excecoes[palavra]

    sufixos = [
        ("eiras", "eiros"),
        ("eira", "eiro"),
        ("onas", "ões"),
        ("ona", "ão"),
        ("esas", "eses"),
        ("esa", "ês"),
    ]

    for fem, masc in sufixos:
        if palavra.endswith(fem):
            candidato = palavra[:-len(fem)] + masc
            if palavra_existe(candidato):
                return candidato

    return palavra  # Retorna a original se nenhuma regra se aplica

def normalizar_texto_masculino(texto):
    # Converte para caixa baixa
    doc = nlp(texto)
    tokens_transformados = []

    for token in doc:
        if not token.is_alpha:
            continue
        lema = token.lemma_
        #print("lema: ", lema)
        # numa versão anterior o código removia as "stop words" do spacy, mas
        # a lista era muito abrangente, contendo palavras como "mal" que
        # afetam o conteudo emocional do texto
        if (
            token.pos_ in ['ADJ', 'NOUN']
            and token.morph.get("Gender") == ['Fem']
            and lema not in nao_converter
        ):
            lema = feminino_para_masculino(lema)
        tokens_transformados.append(lema)
    return ' '.join(tokens_transformados)

def converter(texto):
    texto = texto.lower()
    texto_normalizado = normalizar_texto_masculino(texto)

    return texto_normalizado

text_list = []
count = 1

for index, row in df_og.iterrows():
    print(f'Linha:{count}\n\n')
    texto_tratado = converter(row['text'])
    retorno = {'id_str': row['id_str'], 'text': texto_tratado,'INSULT': row['INSULT'], 'TOXICITY': row['TOXICITY'],'IDENTITY_ATTACK': row['IDENTITY_ATTACK'],'THREAT': row['THREAT'],'PROFANITY': row['PROFANITY'],'SEVERE_TOXICITY': row['SEVERE_TOXICITY']} 
    text_list.append(retorno)
    count += 1

df = pd.DataFrame(text_list)
df.to_csv('data/processed/processed.csv', index = False)

#print(df_og['text'][0])
#texto = df_og["text"][0]
#texto_minusculo = texto.lower()
#print(normalizar_texto_masculino(texto_minusculo))