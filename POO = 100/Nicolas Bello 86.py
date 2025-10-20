from sklearn.linear_model import LinearRegression

def predecir_tiempo(df):
    X = df[['tipo_libro', 'usuario_tipo']]
    y = df['dias_devolucion']
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo
