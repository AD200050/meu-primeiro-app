import streamlit as st

st.title("Meu Primeiro App")

nome = st.text_input("Digite seu nome:")

if nome:
    st.write(f"Olá, {nome}! 👋")
