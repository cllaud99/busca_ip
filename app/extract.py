import pandas as pd
import re
import tabula

termos = ['google','facebook','netflix']

def extrair_pagina_bgp(termos: list) -> pd.DataFrame:   
    """
        Função que le pagina da web e salva em um dataframe:
        Args:
            termos (lista): Lista que todos os termos a serem pesquisados
        Return:
            tabela_resultados (pd.DataFrame): DataFrame com todas as pesquisas
    """

    df_final = pd.DataFrame()

    for termo in termos:
        url = f'https://bgp.he.net/search?search%5Bsearch%5D={termo}&commit=Search'

        try:
            dfs = pd.read_html(url)  
            for df in dfs: 
                df_final = pd.concat([df_final, df], ignore_index=True)

        except Exception as e: 
            print(f'Erro ao processar o termo {termo}: {e}')

    return df_final

def recebe_arquivo(arquivo: str):
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    dfs = tabula.read_pdf(arquivo, pages='all', multiple_tables=True, pandas_options={'header': None})
    dfs_resultante = pd.DataFrame()

    for df in dfs:

        ip_columns = [col for col in df.columns if df[col].astype(str).str.contains(ip_regex).any()]
        result_df = df[ip_columns]
        dfs_resultante = pd.concat([dfs_resultante, result_df], ignore_index=True)


        print(dfs_resultante)


    dfs_resultante.rename(columns={dfs_resultante.columns[0]: 'ips'}, inplace=True)

    dfs_filtrado = dfs_resultante[dfs_resultante['ips'].str.contains(ip_regex, na=False)]

    dfs_filtrado.to_excel('data/data.xlsx')

    return dfs_filtrado


if __name__ == "__main__":
    recebe_arquivo()


