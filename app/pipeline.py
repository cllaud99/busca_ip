from extract import extrair_pagina_bgp
from load import armazenar_dataframe_sqlite_sqlalchemy


def pipeline():

    termos = ['google','facebook','netflix']

    df = extrair_pagina_bgp(termos)

    armazenar_dataframe_sqlite_sqlalchemy(df, 'tbl_resultado_bgp', 'pesquisa_ip.db')

    return 'Ips a serem consultados atualizados internamente'


pipeline()
