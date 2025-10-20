import streamlit as st

def panel(df):
    st.title("Panel de Biblioteca")
    st.metric("Total Préstamos", len(df))
    st.bar_chart(df['genero'].value_counts())
