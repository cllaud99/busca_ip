import tabula


caminho_pdf = tabula.read_pdf('data/25abdcad58265117a33c29589211d29f.pdf', pages='all')

list_df = tabula.read_pdf(caminho_pdf, pages='all', multiple_tables=True)

# Concatena todas as tabelas em um único DataFrame
# Verifica se a lista não está vazia para evitar erros
if list_df:
    df_concatenado = pd.concat(list_df, ignore_index=True)
    print("Todas as tabelas foram concatenadas em um único DataFrame.")
else:
    print("Nenhuma tabela foi encontrada no PDF.")


