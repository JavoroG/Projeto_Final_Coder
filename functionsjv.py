import requests
import pandas as  pd


#Função para criar uma lista com todos os dados dos estados do Brasil, que recebe a sigla e uma lista
def retorna_estado(sigla, lista):

    estados = f"https://brasilapi.com.br/api/ibge/uf/v1/{sigla}"
    req = requests.get(estados)
    code = req.status_code
    if code == 200:
        lista.append(req.json())
    return lista


def tratamento_aeroporto(df, lista):

    # Na coluna localizacao a cidade e as siglas UF estão juntas, vamos separar as siglas e colocar numa coluna nova.
    df[['cidade', 'uf']] = df['localizacao'].str.split("/", expand=True)
    lista.append('Tratamento feito: Cidade e UF separados em duas colunas')

    #Eliminar /n dos dados
    df = df.map(lambda x: x.replace('\n', '') if isinstance(x, str) else x)
    lista.append('Tratamento feito: Eliminar /n dos dados')

    #drop para remover a coluna localizacao ja que temos 2 novas colunas com cidade e uf.
    df = df.drop(['localizacao'], axis=1)
    lista.append('Tratamento feito: Coluna localicao removida pra deixar as colunas cidade e uf')
    return df


def tratamento_cptec(df, lista):

    # Na coluna atualizado em se deve convertir em tipo date
    df['atualizado_em'] = pd.to_datetime(df['atualizado_em'])
    lista.append('Tratamento feito: Valores da coluna "atualizado em" mudados para tipo Datetime')

    # Eliminando a coluna condicao
    df = df.drop(['condicao'], axis=1)
    lista.append('Tratamento feito: Coluna "condicao" eliminada do dataframe')
    return df


def tratamento_estados(df, lista):

    #Se usa list comprehension para extrair do dicionario o valor da chave "nome" que retorna o nome da regiao. Este valor se armazena na variável 'nome_regiao'
    nome_regiao = [regiao['nome'] for regiao in df['regiao']]
    lista.append('Tratamento feito: nome da regiao extraído e armazenado na variável nome_regiao')

    #Se adiciona a nova coluna "nome_regiao" no dataframe df_estados.
    df['nome_regiao'] = nome_regiao
    lista.append('Tratamento feito: Se adicionou a coluna "nome_regiao" no dataframe df_estados')

    return df


def salvar_em_csv(listaDF, listaNome):

    ruta = "C:\\Temp"

    for df, i in zip(listaDF, listaNome):
        
        df.to_csv(f"{ruta}\\{i}.csv")

    return f"Bases salvadas no formato .csv em {ruta}"


def bd_tables(listaCSV, listaTable, conn):

    lista = [] #Lista para indicar que as tabelas foram criadas
    

    for csv, tabela in zip(listaCSV, listaTable):

        nome = tabela #toma o valor de tabela que é o nome que vamos dar para a tabela do tipo String.

        tabela = pd.read_csv(f'C:\\Temp\\{csv}') #leer um csv

        tabela.to_sql(f'{nome}', conn, if_exists='replace', index=False)  #Salvar um dataframe como tabela num banco de dados

        lista.append(nome)

    return f'As tabelas {lista} foram criadas'