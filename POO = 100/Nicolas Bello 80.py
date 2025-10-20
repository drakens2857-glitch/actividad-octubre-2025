import matplotlib.pyplot as plt

def graficar_prestamos_por_mes(df):
    conteo = df['mes'].value_counts().sort_index()
    conteo.plot(kind='bar', title='Préstamos por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.show()
