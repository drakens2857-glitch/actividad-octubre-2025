from sklearn.tree import DecisionTreeClassifier

def predecir_multas(df):
    X = df[['dias_retraso', 'tipo_usuario']]
    y = df['multa']
    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)
    return modelo
