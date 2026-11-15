import pandas as pd
#1
df_raw = pd.read_csv('../data/athlete_events.csv', header=None)

df_atletas = df_raw[0].str.split(',', expand=True)

df_atletas = df_atletas.iloc[:, :15]

df_atletas.columns = df_atletas.iloc[0].str.replace('', '').str.strip()

df_atletas = df_atletas.iloc[1:].reset_index(drop=True)

print(f"Total de registros de atletas: {df_atletas.shape[0]}")

display(df_atletas.head(40))

#2
df_regiones = pd.read_csv("../data/noc_regions.csv")

print(f"Total de regiones/países cargados: {df_regiones.shape[0]}")
display(df_regiones.head(40))

#3 y 4
def obtener_resumen_variables(df, nombre_df):
    resumen = pd.DataFrame({
        'Columna': df.columns,
        'Tipo de Dato': df.dtypes.astype(str),
        'Valores No Nulos': df.notnull().sum(),
        'Valores Nulos': df.isnull().sum(),
        'Total Filas': len(df)
    })
    print(f"=== Tabla de Variables: {nombre_df} ===")
    display(resumen.reset_index(drop=True))

obtener_resumen_variables(df_atletas, "Atletas")

obtener_resumen_variables(df_regiones, "Regiones")

print("\n=== Estadísticas Básicas: Atletas ===")
display(df_atletas.describe(include='all'))

print("\n=== Estadísticas Básicas: Regiones ===")
display(df_regiones.describe(include='all'))

#4 IMC
df_atletas.columns = df_atletas.columns.str.replace('"', '').str.strip()

df_atletas['Height'] = pd.to_numeric(df_atletas['Height'], errors='coerce')
df_atletas['Weight'] = pd.to_numeric(df_atletas['Weight'], errors='coerce')

df_atletas['IMC'] = df_atletas['Weight'] / (df_atletas['Height'] / 100) ** 2

display(df_atletas[['Name', 'Sport', 'Height', 'Weight', 'IMC']].head(40))

#5
df_completo = pd.merge(df_atletas, df_regiones, on='NOC', how='left')

print(f"Filas originales en atletas: {len(df_atletas)}")
print(f"Filas después del merge: {len(df_completo)}")

filas_sin_region = df_completo['region'].isnull().sum()
print(f"Filas sin región asignada: {filas_sin_region}")

display(df_completo[['Name', 'NOC', 'region', 'Sport']].head(40))

#6
df_completo['medalla'] = df_completo['Medal'].notnull().astype(int)

total_filas = len(df_completo)
atletas_unicos = df_completo['ID'].nunique()

print(f"\nTotal de registros (filas): {total_filas}")
print(f"Cantidad de atletas únicos (ID): {atletas_unicos}")

display(df_completo[['Name', 'Medal', 'medalla']].head(40))