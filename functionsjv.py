import requests
import pandas as  pd


#Função para criar uma lista com todos os dados dos estados do Brasil, que recebe a sigla e uma lista
def retorna_estado(sigla, lista):
    """
        Esta função conecta com o API de Estados do Brasil e passa como parâmetro
        a sigla UF para que retorne os dados de essa unidade federativa(UF) numa lista 
    """
    estados = f"https://brasilapi.com.br/api/ibge/uf/v1/{sigla}"
    req = requests.get(estados)
    code = req.status_code
    if code == 200:
        lista.append(req.json())
    return lista


def tratamento_aeroporto(df, lista):

    """
        Esta função realiza o tratamento requerido para a base Aeroporto, que neste caso
        é separar dados da coluna localizacao, eliminar carácter /n, remover colunas, e remover
        acentos das letras minúsculas
    """

    # Na coluna localizacao a cidade e as siglas UF estão juntas, vamos separar as siglas e colocar numa coluna nova.
    df[['cidade', 'uf']] = df['localizacao'].str.split("/", expand=True)
    lista.append('Tratamento feito: Cidade e UF separados em duas colunas')

    #Eliminar /n dos dados
    df = df.map(lambda x: x.replace('\n', '') if isinstance(x, str) else x)
    lista.append('Tratamento feito: Eliminar /n dos dados')

    #drop para remover a coluna localizacao ja que temos 2 novas colunas com cidade e uf.
    df = df.drop(['localizacao'], axis=1)
    lista.append('Tratamento feito: Coluna localicao removida pra deixar as colunas cidade e uf')

    #Eliminar acentos
    df = df.map(lambda x: x.replace('á', 'a') if isinstance(x, str) else x)
    df = df.map(lambda y: y.replace('é', 'e') if isinstance(y, str) else y)
    df = df.map(lambda z: z.replace('í', 'i') if isinstance(z, str) else z)
    df = df.map(lambda w: w.replace('ó', 'o') if isinstance(w, str) else w)
    df = df.map(lambda v: v.replace('ú', 'u') if isinstance(v, str) else v)
    lista.append('Tratamento feito: Acentos removidos')

    return df


def tratamento_cptec(df, lista):

    """
        Esta função realiza o tratamento requerido para a base CPTEC. 
        Muda o tipo de dado para date da 'coluna atalizado em', remove a 
        coluna 'condicao', e remove o acento das letras minúsculas 
    """

    # Na coluna atualizado em se deve convertir em tipo date
    df['atualizado_em'] = pd.to_datetime(df['atualizado_em'])
    lista.append('Tratamento feito: Valores da coluna "atualizado em" mudados para tipo Datetime')

    # Eliminando a coluna condicao
    df = df.drop(['condicao'], axis=1)
    lista.append('Tratamento feito: Coluna "condicao" eliminada do dataframe')

    #Eliminar acentos
    df = df.map(lambda x: x.replace('á', 'a') if isinstance(x, str) else x)
    df = df.map(lambda y: y.replace('é', 'e') if isinstance(y, str) else y)
    df = df.map(lambda z: z.replace('í', 'i') if isinstance(z, str) else z)
    df = df.map(lambda w: w.replace('ó', 'o') if isinstance(w, str) else w)
    df = df.map(lambda v: v.replace('ú', 'u') if isinstance(v, str) else v)
    lista.append('Tratamento feito: Acentos removidos')
    
    return df


def tratamento_estados(df, lista):

    """
        Esta função usa list comprenhension para extrair o nome da região de um dicionario, 
        cria uma nova coluna com o nome da regiã extraída, e e remove o acento das letras minúsculas
    """

    #Se usa list comprehension para extrair do dicionario o valor da chave "nome" que retorna o nome da regiao. Este valor se armazena na variável 'nome_regiao'
    nome_regiao = [regiao['nome'] for regiao in df['regiao']]
    lista.append('Tratamento feito: nome da regiao extraído e armazenado na variável nome_regiao')

    #Se adiciona a nova coluna "nome_regiao" no dataframe df_estados.
    df['nome_regiao'] = nome_regiao
    lista.append('Tratamento feito: Se adicionou a coluna "nome_regiao" no dataframe df_estados')

    #Eliminar acentos
    df = df.map(lambda x: x.replace('á', 'a') if isinstance(x, str) else x)
    df = df.map(lambda y: y.replace('é', 'e') if isinstance(y, str) else y)
    df = df.map(lambda z: z.replace('í', 'i') if isinstance(z, str) else z)
    df = df.map(lambda w: w.replace('ó', 'o') if isinstance(w, str) else w)
    df = df.map(lambda v: v.replace('ú', 'u') if isinstance(v, str) else v)
    lista.append('Tratamento feito: Acentos removidos')

    return df


def salvar_em_csv(listaDF, listaNome):

    """
        Esta função recebe uma lista con dataframes e outra lista com nomes tipo string, 
        e cria um arquivo .csv com o nome requerido para cada dataframe da lista.
    """

    ruta = "C:\\Temp"

    for df, i in zip(listaDF, listaNome):
        
        df.to_csv(f"{ruta}\\{i}.csv")

    return f"Bases salvadas no formato .csv em {ruta}"


def bd_tables(listaCSV, listaTable, conn):

    """
        Esta função recebe um arquivo .csv e o converte em uma tabela do banco de dados conectado.
    """

    lista = [] #Lista para indicar que as tabelas foram criadas
    

    for csv, tabela in zip(listaCSV, listaTable):

        nome = tabela #toma o valor de tabela que é o nome que vamos dar para a tabela do tipo String.

        tabela = pd.read_csv(f'C:\\Temp\\{csv}') #leer um csv

        tabela.to_sql(f'{nome}', conn, if_exists='replace', index=False)  #Salvar um dataframe como tabela num banco de dados

        lista.append(nome)

    return f'As tabelas {lista} foram criadas'