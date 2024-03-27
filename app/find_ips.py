         
import requests
from bs4 import BeautifulSoup
import pandas as pd

def consulta_ips(ip):
    """
        Função que recebe recebe um endereço de IP e realiza a consulta no site do BGP
        Args:
            ip (str): Ip a ser consultado
        Returns:
            lista com dados
    """
    url = f'https://bgp.he.net/ip/{ip}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        
        if table:
            rows = table.find_all('tr')[1:]
            dados_extraidos = []
            
            for row in rows:
                cells = row.find_all(['td', 'th'])
                linha = [cell.get_text(strip=True) for cell in cells]
                dados_extraidos.append(linha)
                
            return {'ip': ip, 'dados': dados_extraidos}

    return {'ip': ip, 'dados': []}



def trata_df(df):

    """
        Função que recebe um dataframe, iterra sobre ele e acrescenta as colunas origin, announcement, description
        Args:
            df (pd.DataFrame) dados a serem tratados
        Returns:
            df (pd.DataFrame) dados com colunas adicionadas
    """
    
    print(df)

    resultados = []
    origin_as_list = []
    announcement_list = []
    description_list = []

    for index, row in df.iterrows():

        resultado = consulta_ips(row['ips']) 

        origin_as_list.append(resultado['dados'][1][0])
        announcement_list.append(resultado['dados'][1][1])
        description_list.append(resultado['dados'][1][2])
        
        print(f'pesquisando {row}')

        print('***************************************************************')


    df['origin'] = origin_as_list
    df['announcement'] = announcement_list
    df['description'] = description_list

    df.to_excel('data/screaping_2.xlsx')

    return df


