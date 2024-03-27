import pandas as pd
import re
import tabula
import requests
from bs4 import BeautifulSoup


def consulta_ips(ip):
    
    """
    Função que recebe um endereço IP e retorna uma tabela com infos sobre:
    Args:
        ip (str): endereço ip a ser consultado
    Return:
        tbl_extraida: tabela com as infos extraidas
    """
    url = 'https://bgp.he.net/ip/{ip}'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')[1:]         

            for row in rows:
                cells = row.find_all(['td', 'th']) 
                
                dados_extraidos.append(linha)
                
            # Retornando os dados como um dicionário
            return {'ip': ip, 'dados': dados_extraidos}
    # Retorno em caso de falha
    return {'ip': ip, 'dados': []}

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

def recebe_arquivo(arquivo: str) -> pd.DataFrame:

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


