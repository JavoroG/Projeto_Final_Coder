import requests
import pandas as pd
import bs4 as bs

#Função que recebe uma URL HTML, conecta e extrai dados de uma tabela
def basehtml(url):
    resp = requests.get(url)
    resp = resp.text
    soup = bs.BeautifulSoup(resp, 'lxml')
    table = soup.find('table')

    
            
    aeroportos_nome_usual = []       #Lista para o nome usual 
    aeroportos_nome_oficial = []     #Lista para o nome oficial do aeroporto 
    codigo_icao = []                 #Lista para o código ICAO (International Civil Aviation Organization) do aeroporto 
    localizacao = []                #Cidade e estado onde se localiza o aeroporto



    for row in table.findAll('tr')[1:]:
        nome_usual = row.findAll('td')[1].text
        nome_oficial = row.findAll('td')[2].text
        icao = row.findAll('td')[3].text
        localiza = row.findAll('td')[5].text

        aeroportos_nome_usual.append(nome_usual)
        aeroportos_nome_oficial.append(nome_oficial)
        codigo_icao.append(icao)
        localizacao.append(localiza)
    
        df2 = pd.DataFrame(list(zip(aeroportos_nome_usual, aeroportos_nome_oficial, codigo_icao, localizacao)),
                      columns=['nome usual', 'nome oficial', 'codigo', 'localizacao'])

    return df2