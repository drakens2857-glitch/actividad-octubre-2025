def comparar_sedes(df):
    return df.groupby('sede')['libro'].count().sort_values(ascending=False)
