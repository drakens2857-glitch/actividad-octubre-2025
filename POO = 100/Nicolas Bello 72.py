import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

class DashboardBiblioteca:
    def __init__(self, gestor_prestamos):
        self.gestor = gestor_prestamos

    def run(self):
        st.set_page_config(page_title="Biblioteca SENA", page_icon="📚", layout="wide")
        st.title("Dashboard de Préstamos - Biblioteca SENA Mosquera")

        df = self.gestor.df_prestamos
        if df.empty:
            st.warning("No hay datos de préstamos registrados.")
            return

        st.subheader("Estadísticas Generales")
        st.metric("Total de Préstamos", len(df))
        st.metric("Tasa de Devolución (%)", f"{(df['devuelto'].sum() / len(df)) * 100:.2f}")
        st.metric("Total en Multas", f"${df['multa'].sum():.2f}")

        st.subheader("Distribución por Tipo de Libro")
        tipo_counts = df['tipo_libro'].value_counts().reset_index()
        tipo_counts.columns = ['Tipo', 'Cantidad']
        fig = px.bar(tipo_counts, x='Tipo', y='Cantidad', color='Tipo', title="Préstamos por Tipo de Libro")
        st.plotly_chart(fig)

        st.subheader("Historial de Préstamos")
        st.dataframe(df.sort_values(by='fecha', ascending=False))
