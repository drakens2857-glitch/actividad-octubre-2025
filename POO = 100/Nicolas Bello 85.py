from sklearn.linear_model import LogisticRegression

def entrenar_clasificador(df):
    X = df[['prestamos', 'devoluciones']]
    y = df['activo']
    modelo = LogisticRegression()
    modelo.fit(X, y)
    return modelo
