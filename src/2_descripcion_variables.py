import pandas as pd

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