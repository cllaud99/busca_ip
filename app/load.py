from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

def armazenar_dataframe_sqlite_sqlalchemy(df_armazenar, tbl_nome, db_nome='meu_banco.db'):
    """
    Armazena um DataFrame em uma tabela do banco de dados SQLite usando SQLAlchemy.
    
    Args:
        df_armazenar (pd.DataFrame): DataFrame a ser armazenado.
        tbl_nome (str): Nome da tabela onde os dados serão armazenados.
        db_nome (str): Nome do arquivo do banco de dados SQLite. O padrão é 'meu_banco.db'.
    """

    engine = create_engine(f'sqlite:///{db_nome}')

    df_armazenar['created_at'] = pd.Timestamp.now()
    
    df_armazenar.to_sql(tbl_nome, engine, if_exists='replace', index=False)
    
    print(f"Dados armazenados com sucesso na tabela '{tbl_nome}' do banco '{db_nome}' usando SQLAlchemy.")
