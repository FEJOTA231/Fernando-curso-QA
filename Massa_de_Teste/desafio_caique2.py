import pandas as pd

df = pd.read_csv("Massa_de_Teste/dados_ficticios.csv")
filtrada = df[(df['idade'] > 40) & (df['renda'] > 5000)]
print(filtrada)