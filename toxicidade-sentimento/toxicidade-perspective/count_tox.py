import pandas as pd

df = pd.read_csv('data/processed/processed.csv')

#linhas com mais de 0.7

insult_df = df[df[['INSULT']].sum(axis=1) > 0.7]
toxicity_df = df[df[['TOXICITY']].sum(axis=1) > 0.7]
identity_attack_df = df[df[['IDENTITY_ATTACK']].sum(axis=1) > 0.7]
threat_df = df[df[['THREAT']].sum(axis=1) > 0.7]
profanity_df = df[df[['PROFANITY']].sum(axis=1) > 0.7]
severe_toxicity_df = df[df[['SEVERE_TOXICITY']].sum(axis=1) > 0.7]

percent_insult = len(insult_df)/len(df)*100
percent_toxicity = len(toxicity_df)/len(df)*100
percent_identity_attack = len(identity_attack_df)/len(df)*100
percent_threat = len(threat_df)/len(df)*100
percent_profanity = len(profanity_df)/len(df)*100
percent_severe_toxicity = len(severe_toxicity_df)/len(df)*100


print(f"Quantidade de tweets de São Paulo: {len(df)}")
print(f"Quantidade e porcentagem de tweets com Toxicidade:{len(toxicity_df)} ({percent_toxicity:.2f}%)")
print(f"Quantidade e porcentagem de tweets com Insulto:{len(insult_df)} ({percent_insult:.2f}%)")
print(f"Quantidade e porcentagem de tweets com Ataque de identidade:{len(identity_attack_df)} ({percent_identity_attack:.2f}%)")
print(f"Quantidade e porcentagem de tweets com Ameaça:{len(threat_df)} ({percent_threat:.2f}%)")
print(f"Quantidade e porcentagem de tweets com Profanidade:{len(profanity_df)} ({percent_profanity:.2f}%)")
print(f"Quantidade e porcentagem de tweets com Toxicidade severa:{len(severe_toxicity_df)} ({percent_severe_toxicity:.2f}%)")