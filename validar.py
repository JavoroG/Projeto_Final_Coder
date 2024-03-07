import requests
import pandas as  pd
from plyer import notification 
from datetime import datetime


def alerta(code, url, etapa):

    """
        A função de alerta gera uma notificação do Windows com o estado de uma conexão a uma URL, 
        indicando sucesso se o código for igual a 200.
    """

    now = (datetime.now())
    data_hora = now.strftime("%d/%m/%y %H:%M:%S")
    msg = f'Falha no carregamento da base {url} na etapa {etapa}. \n{data_hora}'
    

    if code == 200:
        title = 'Conexão exitosa'
        msg = f'Voce esta conectado na base {url}. \n{data_hora}'
    elif code >= 400:
        title = f'Não tem permissão de acessar na base: {url}'
    elif code >= 500:
        title = f'Erro de conexão com o server {url}'

    notification.notify(
        title = title,
        message = msg,
        app_name= 'Alerta',
        timeout = 5
    )

def conexao(url, list, bases):
    
    """
        Esta função realiza a conexão com uma URL, pasa para o formato JSON
        e chama a função alerta
    """

    req = requests.get(url)
    code = req.status_code
    list.append({url:code})
    if bases != 0:
        bases.append(req.json()) # Obtém os dados da resposta no formato JSON
    alerta(code, url, 'Extracao')    
    return list
#, bases    