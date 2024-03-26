import pandas as pd
from sqlalchemy import create_engine, text

def busca_correspondencia(df):

    engine = create_engine('sqlite:///pesquisa_ip.db', echo=True)

    valores_existentes = []

    with engine.connect() as connection:
        for valor in df['ips']:
            # Utilizando a função text para criar um objeto SQL executável
            query = text(f"SELECT EXISTS(SELECT 1 FROM tbl_resultado_bgp WHERE Result = :valor)")
            
            # Execute a query utilizando parâmetros nomeados para evitar SQL Injection
            result = connection.execute(query, {'valor': valor}).fetchone()
            existe = result[0] == 0  # True se o valor existe, False caso contrário
            valores_existentes.append(existe)

    # Adiciona o resultado ao DataFrame
    df['pode bloquear'] = valores_existentes

    df.to_excel('data/data_processada.xlsx')

    print(df)

    return df