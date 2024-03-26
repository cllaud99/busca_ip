import pandas as pd

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

