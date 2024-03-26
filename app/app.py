import streamlit as st
from pipeline import pipeline
from extract import recebe_arquivo
import pandas as pd


st.title('verica IPs do gbp')


uploaded_file = st.file_uploader("Faça o upload do arquivo Excel aqui:", type=['xlsx', 'xls', 'pdf'])

if st.button('Atualizar dados'):
    fluxo = pipeline()
    st.write(fluxo)

if uploaded_file is not None:
    # Ler o arquivo Excel
    df = recebe_arquivo(uploaded_file)
    st.write(df)