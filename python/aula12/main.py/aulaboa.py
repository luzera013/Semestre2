import pandas as pd

dados = {
    "regiao": ["Centro", "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Industrial"],
    "pm25": [18, 42, 25, 55, 20, 68],
    "pm10": [35, 70, 45, 90, 40, 110],
    "temperatura": [29, 31, 27, 32, 28, 34],
    "umidade": [60, 48, 65, 45, 62, 40]
}

df = pd.DataFrame(dados)

# 1. Classificação PM2.5
df['status_pm25'] = df['pm25'].apply(
    lambda x: "Baixo" if x <= 20 else ("Moderado" if x <= 40 else "Alto")
)

# 2. Classificação PM10
df['status_pm10'] = df['pm10'].apply(
    lambda x: "Baixo" if x <= 20 else ("Moderado" if x <= 40 else "Alto")
)

# 3. Correção da Região: Avaliando múltiplas condições em uma linha
df['status_regiao'] = df['regiao'].apply(
    lambda x: "Zona Central" if x == "Centro" else ("Zona Industrial" if x == "Industrial" else "Outra Zona")
)
df['clima'] = df['temperatura'].apply(
    lambda x: "baixo" if x <= 30 else ("Normal" if x >= 30 else "Alto"))

print(df)

####################################################################

import pandas as pd

dados = {
    "regiao": ["Centro", "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Industrial"],
    "pm25": [18, 42, 25, 55, 20, 68],
    "pm10": [35, 70, 45, 90, 40, 110],
    "temperatura": [29, 31, 27, 32, 28, 34],
    "umidade": [60, 48, 65, 45, 62, 40]
}

df = pd.DataFrame(dados)

def nive_pm25(valor):
    if valor <= 20:
        return "Baixo"
    elif valor <= 40:
        return "Moderado"
    else:
        return "Alto"

#df['nive_pm25'] = df['pm25'].apply(nive_pm25(df['pm25']))
#df['nive_pm25'] = df['pm25'].apply(nive_pm25)

##################################################################################################

# Usando lambda

df['nive_pm25'] = df['pm25'].apply(lambda x: 'baixo' if x <= 20 else('moderado' if x <= 40 else 'alto'))


##############################################################################################
#    lambda x: "Baixo" if x <= 20 else ("Moderado" if x <= 40 else "Alto")
import pandas as pd

dados = {
    "regiao": ["Centro", "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Industrial"],
    "pm25": [18, 42, 25, 55, 20, 68],
    "pm10": [35, 70, 45, 90, 40, 110],
    "temperatura": [29, 31, 27, 32, 28, 34],
    "umidade": [60, 48, 65, 45, 62, 40]
}

df = pd.DataFrame(dados)

df['avaliar_risco'] = df['pm25'].apply(
    lambda x: "risco_alto"
    if x >= 50
    else ("risco_moderado" if x <= 30 else "risco baixo")
)

print(df)
#erro

###############################
import pandas as pd

dados = {
    "regiao": ["Centro", "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Industrial"],
    "pm25": [18, 42, 25, 55, 20, 68],
    "pm10": [35, 70, 45, 90, 40, 110],
    "temperatura": [29, 31, 27, 32, 28, 34],
    "umidade": [60, 48, 65, 45, 62, 40]
}

df = pd.DataFrame(dados)

def avaliar_risco(linha):
    if linha["pm25"] > 50 and linha["temperatura"] > 30:
        return "Risco alto"
    elif linha["pm25"] > 30:
        return "Risco moderado"
    else:
        return "risco baixo"
    
df["risco"] = df.apply(avaliar_risco, axis=1)

print(df)
   
