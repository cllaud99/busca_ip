# Verificador de IPs BGP


## Descrição

O "Verificador de IPs BGP" é uma ferramenta desenvolvida para facilitar a análise e o processamento de arquivos contendo endereços IP, verificando detalhes de roteamento BGP para cada IP através de consultas automatizadas. Utilizando uma combinação de Python, pandas, Tabula para leitura de PDFs, e BeautifulSoup para raspagem web, este projeto permite aos usuários carregar arquivos `.pdf` ou `.xlsx` para extrair IPs, consultar informações detalhadas de roteamento BGP online e, em seguida, gerar um relatório enriquecido dessas informações. Integrado com Streamlit, o projeto também oferece uma interface fácil para os usuários visualizarem e interagirem com os dados processados.


## Pré-requisitos

Para executar este projeto, é necessário ter instalado em sua máquina:

- Python 3.11 ou superior
- Poetry para gerenciamento de dependências

## Instalação

Para configurar o ambiente e instalar as dependências necessárias, siga os passos abaixo:

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/cllaud99/busca_ip
cd busca_ip
```

2. Utilize o Poetry para instalar as dependências do projeto:
```bash
poetry install
```
Isso criará um ambiente virtual e instalará todas as dependências listadas no arquivo pyproject.toml.

## Execução

Para executar o aplicativo Streamlit e começar a utilizar a ferramenta, use o seguinte comando:
```bash
poetry run streamlit run app.py
```
Isso iniciará o servidor do Streamlit e abrirá a interface no seu navegador padrão.

## Uso
1. Acesse a interface do Streamlit através do navegador.
2. Faça o upload do arquivo contendo os IPs que deseja verificar. O arquivo deve ser no formato .pdf ou .xlsx.
3. A ferramenta processará o arquivo, consultará as informações de BGP para cada IP encontrado e exibirá um DataFrame com os resultados.
4. Você pode baixar os resultados processados diretamente pela interface do Streamlit.

## Aplicação

A Aplicação pode ser consultada no [link](https://buscaipbgp.streamlit.app/)

![Texto alternativo](pics/print.png "Print da imagem")