import pandas as pd
from datetime import datetime

class AnalizadorBiblioteca:
    def __init__(self):
        self.df_prestamos = pd.DataFrame(columns=[
            'fecha', 'libro', 'usuario', 'tipo_libro', 'devuelto', 'multa'
        ])

    def registrar_prestamo(self, libro, usuario, tipo_libro):
        nuevo_registro = pd.DataFrame([{
            'fecha': datetime.now(),
            'libro': libro,
            'usuario': usuario,
            'tipo_libro': tipo_libro,
            'devuelto': False,
            'multa': 0
        }])
        self.df_prestamos = pd.concat([self.df_prestamos, nuevo_registro], ignore_index=True)

    def obtener_estadisticas(self):
        if len(self.df_prestamos) == 0:
            return "No hay datos para analizar"
        stats = {
            'total_prestamos': len(self.df_prestamos),
            'por_tipo': self.df_prestamos['tipo_libro'].value_counts().to_dict(),
            'tasa_devolucion': (self.df_prestamos['devuelto'].sum() / len(self.df_prestamos)) * 100,
            'total_multas': self.df_prestamos['multa'].sum()
        }
        return stats

    def libros_mas_prestados(self, top_n=5):
        return self.df_prestamos['libro'].value_counts().head(top_n)

    def exportar_a_excel(self, nombre_archivo='reporte_biblioteca.xlsx'):
        self.df_prestamos.to_excel(nombre_archivo, index=False)
        return f"Datos exportados a {nombre_archivo}"
