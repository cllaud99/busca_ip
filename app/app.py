import streamlit as st
from pipeline import pipeline
from extract import recebe_arquivo
from transform import busca_correspondencia
import pandas as pd


st.title('verica IPs do gbp')

st.write('Clique nesse botão para consultar na internet informações mais recentes de IPs')
if st.button('Atualiza dados do bpg'):
    fluxo = pipeline()
    st.write(fluxo)


uploaded_file = st.file_uploader("Faça o upload do arquivo Excel aqui:", type=['xlsx', 'xls', 'pdf'])


if uploaded_file is not None:

    df = recebe_arquivo(uploaded_file)
    df_final = busca_correspondencia(df)
    st.write(df_final)