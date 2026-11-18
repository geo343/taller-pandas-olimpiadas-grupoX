import pandas as pd
#Punto 1: Cargar cada conjunto de datos en un DataFrame distinto (df_atletas y df_regiones)
df_raw = pd.read_csv('../data/athlete_events.csv', header=None)

df_atletas = df_raw[0].str.split(',', expand=True)

df_atletas = df_atletas.iloc[:, :15]

df_atletas.columns = df_atletas.iloc[0].str.replace('', '').str.strip()

df_atletas = df_atletas.iloc[1:].reset_index(drop=True)

print(f"Total de registros de atletas: {df_atletas.shape[0]}")

display(df_atletas.head(40))

df_regiones = pd.read_csv("../data/noc_regions.csv")

print(f"Total de regiones/países cargados: {df_regiones.shape[0]}")
display(df_regiones.head(40))