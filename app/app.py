import streamlit as st
from pipeline import pipeline


st.title('verica IPs do gbp')


if st.button('Atualizar dados'):
    fluxo = pipeline()
    st.write(fluxo)