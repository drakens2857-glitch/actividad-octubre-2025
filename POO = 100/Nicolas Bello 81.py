def prestamos_por_edad(df):
    df['grupo'] = pd.cut(df['edad'], bins=[0, 18, 30, 50, 100], labels=['Joven', 'Adulto Joven', 'Adulto', 'Mayor'])
    return df.groupby('grupo')['libro'].count()
