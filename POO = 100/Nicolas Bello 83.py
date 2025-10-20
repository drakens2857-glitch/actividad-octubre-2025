def libros_con_baja_rotacion(df, umbral=2):
    conteo = df['libro'].value_counts()
    return conteo[conteo < umbral].index.tolist()
