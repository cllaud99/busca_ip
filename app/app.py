import streamlit as st
from pipeline import pipeline
from extract import recebe_arquivo
from transform import busca_correspondencia
import pandas as pd
from find_ips import trata_df, consulta_ips

st.title('verica IPs do gbp')


uploaded_file = st.file_uploader("Faça o upload do arquivo Excel aqui:", type=['xlsx', 'xls', 'pdf'])


if uploaded_file is not None:

    df = recebe_arquivo(uploaded_file)
    df_final = trata_df(df)
    st.write(df_final)