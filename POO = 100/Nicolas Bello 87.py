from sklearn.cluster import KMeans

def agrupar_libros(df):
    modelo = KMeans(n_clusters=3)
    df['grupo'] = modelo.fit_predict(df[['paginas', 'popularidad']])
    return df
