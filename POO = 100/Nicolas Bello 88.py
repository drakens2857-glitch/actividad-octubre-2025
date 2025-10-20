from sklearn.neighbors import NearestNeighbors

def recomendar(df, usuario_id):
    matriz = df.pivot_table(index='usuario', columns='libro', values='valoracion').fillna(0)
    modelo = NearestNeighbors(metric='cosine')
    modelo.fit(matriz)
    distancias, vecinos = modelo.kneighbors([matriz.loc[usuario_id]], n_neighbors=3)
    return matriz.iloc[vecinos[0]].mean().sort_values(ascending=False).head()
