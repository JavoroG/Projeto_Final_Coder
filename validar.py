import requests
import pandas as  pd
from plyer import notification 
from datetime import datetime


def alerta(code, url, etapa):

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
    
    req = requests.get(url)
    code = req.status_code
    list.append({url:code})
    if bases != 0:
        bases.append(req.json())
    alerta(code, url, 'Extracao')    
    return list
#, bases    