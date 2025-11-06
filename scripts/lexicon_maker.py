import json

# Caminho para o arquivo de entrada
caminho_arquivo = "toxicidade-sentimento/sentimento-liwc/NRC-Emotion-Lexicon/NRC-Emotion-Lexicon/OneFilePerLanguage/Portuguese-NRC-EmoLex.txt"

# Dicionário final com as palavras em português como chave
lexicon = {}

# Lê o conteúdo do arquivo
with open(caminho_arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Extrai os cabeçalhos das emoções (entre a primeira e a penúltima coluna)
cabecalhos = linhas[0].strip().split("\t")
emocoes = cabecalhos[1:-1]

# Processa as linhas de dados
for linha in linhas[1:]:
    colunas = linha.strip().split("\t")
    palavra_portugues = colunas[-1]
    valores = list(map(int, colunas[1:-1]))

    # Filtra as emoções com valor 1
    emocoes_ativas = [emocao for emocao, valor in zip(emocoes, valores) if valor == 1]

    if emocoes_ativas:
        lexicon[palavra_portugues] = emocoes_ativas

# Salva em JSON se quiser
with open("lexicon_portugues.json", "w", encoding="utf-8") as f:
    json.dump(lexicon, f, ensure_ascii=False, indent=4)

print("Lexicon em português gerado com sucesso!")