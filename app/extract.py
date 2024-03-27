import pandas as pd
import re
import tabula
import requests
from bs4 import BeautifulSoup

def recebe_arquivo(arquivo: str) -> pd.DataFrame:

    """
        Função que recebe um arquivo .pdf ou .xlsx busca por colunas que tem ips e devolve uma relação tratada de ips
        Args:
            arquivo (str) Arquivo que contem os dados
        Return:
            dfs_filtrado (pd.DataFrame) DataFrame tratado
    """

    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    dfs_resultante = pd.DataFrame()


    if arquivo.name.endswith(".pdf"):
        dfs = tabula.read_pdf(arquivo, pages='all', multiple_tables=True, pandas_options={'header': None})

        for df in dfs:

            ip_columns = [col for col in df.columns if df[col].astype(str).str.contains(ip_regex).any()]
            result_df = df[ip_columns]
            dfs_resultante = pd.concat([dfs_resultante, result_df], ignore_index=True)


            print(dfs_resultante)

    elif arquivo.name.endswith(".xlsx"):

        dfs = pd.read_excel(arquivo, header= None)

        ip_columns = [col for col in dfs.columns if dfs[col].astype(str).str.contains(ip_regex).any()]
        result_df = dfs[ip_columns]
        dfs_resultante = result_df

    dfs_resultante.rename(columns={dfs_resultante.columns[0]: 'ips'}, inplace=True)

    dfs_filtrado = dfs_resultante[dfs_resultante['ips'].str.contains(ip_regex, na=False)]

    dfs_filtrado.to_excel('data/data.xlsx')

    return dfs_filtrado

if __name__ == "__main__":
    recebe_arquivo('data/data.xlsx')


