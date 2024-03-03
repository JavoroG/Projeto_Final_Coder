<h1>Centro de Previsão de tempo e estudos climáticos (CPTEC) nos aeroportos do Brasil</h1>

<h3>Objetivo: </h3>
<p>Criar um pipeline de dados que abrange as fases de extração, tratamento, alertas, deploys e documentação.</p>

<hr>

<p>Este projeto permite obter informações sobre as condições climáticas nos aeroportos do Brasil. Para isso, são utilizadas três fontes diferentes para a extração dos dados. As duas primeiras são APIs: uma para informações climáticas (CPTEC) disponível em <a href="https://brasilapi.com.br/api/cptec/v1/clima/capital">(CPTEC)</a>, e outra para obter dados dos estados do Brasil, acessível em <a href="https://brasilapi.com.br/api/ibge/uf/v1/{code}">(Estados por code)</a>. A terceira fonte é uma URL de um site da Web (<a href="https://pt.wikipedia.org/wiki/Lista_de_aeroportos_do_Brasil_por_c%C3%B3digo_aeroportu%C3%A1rio_ICAO">Tabela ICAO</a>), de onde são extraídos os códigos da International Civil Aviation Organization (ICAO) para o Brasil, de uma tabela no formato HTML.</p>

<hr>

<h3>Tecnologias utilizadas:</h3>
<ul>
<li>Python 3.12.1</li>
<li>Visual Studio Code 1.87</li>
</ul>

<hr>

<h3 >Bibliotecas utilizadas:</h3>
<ul>
<li>pandas</li>
<li>bs4</li>
<li>sqlite3</li>
<li>requests</li>
<li>datetime</li>
<li>plyer</li>
</ul>

> [!NOTE]
> As bibliotecas acima devem ser importadas para poder utilizar suas clases.

<hr>

<h3>Arquivos do projeto:</h3>
<ul>
  <li>
    <strong><a href = "https://github.com/JavoroG/Projeto_Final_Coder/blob/main/functionsjv.py">functionsjv.py</a></strong><p>Contém as funções que permitem criar a base de estados, realizar o tratamento das bases, salvar no formato .csv e criar as tabelas.</p>
  </li> 
  <li>
    <strong><a href = "https://github.com/JavoroG/Projeto_Final_Coder/blob/main/validar.py">validar.py</a></strong> <p>Contém a função que valida se a conexão das URLs (APIs, HTML) foi bem-sucedida ou não e gera um alerta do Windows com os comentários.</p>
  </li>
  <li>
    <strong><a href = "https://github.com/JavoroG/Projeto_Final_Coder/blob/main/reqhtml.py">reqhtml.py</a></strong> <p>Contém uma função que extrai uma tabela no formato HTML, armazena os dados numa lista e retorna um dataframe com esses dados.</p>
  </li>
  <li>
    <strong><a href = "https://github.com/JavoroG/Projeto_Final_Coder/blob/main/requirements.txt">requirements.txt</a></strong> <p>Contém as bibliotecas com suas respectivas versões utilizadas no projeto.</p>
  </li>
</ul>

> [!WARNING]
> Os arquivos acima contém as funções necessarias para a validação, extração, tratamento e criação das tabelas, com os dados dos APIs.

<hr>

<h3>APIs/HTML</h3>

<p>No projeto foram usados dois APIs do Brasil API para CPTEC e Estados, e a URL de Wikipedia com uma tabela com os códigos ICAO para os aeroportos do Brasil</p>

<h4>Aeroportos</h4>

##### Retorna um arquivo HTML com a tabela dos aeroportos do Brasil com seus códigos ICAO
```
https://pt.wikipedia.org/wiki/Lista_de_aeroportos_do_Brasil_por_c%C3%B3digo_aeroportu%C3%A1rio_ICAO)https://pt.wikipedia.org/wiki/Lista_de_aeroportos_do_Brasil_por_c%C3%B3digo_aeroportu%C3%A1rio_ICAO
```

<h4>CPTEC</h4>

##### Retorna um arquivo JSON com as condições climáticas dos aeroportos atualizadas

```
https://brasilapi.com.br/api/cptec/v1/clima/capital
```
<h4>Estados</h4>

##### Retorna um dicionário com os dados de cada estado, mas precissa ser passado o código UF ja que só retorna um estado por consulta.

```
https://brasilapi.com.br/api/ibge/uf/v1/{code}
```

<hr>

<h3>Execução</h3>

<img src="https://github.com/JavoroG/Projeto_Final_Coder/blob/main/Flowchart.png" alt="Descrição da Imagem"> 

<hr>



<hr>

<h3>Testes</h3>

<h4>Verificando APIs</h4>

<p>Para verificar se a API está funcionando corretamente, chama-se a função 'conexao', passando a URL e uma lista chamada 'bases' como parâmetros.</p>

<code>val.conexao(cptec, list, bases)</code> 

<p>A função conexao realiza uma solicitação HTTP Get para a URL e se é bem sucedida o status code será 200. logo chama-se a função alerta</p>

```
def conexao(url, list, bases):
    
    req = requests.get(url)
    code = req.status_code
    list.append({url:code})
    if bases != 0:
        bases.append(req.json())
    alerta(code, url, 'Extracao')    
    return list
```

<p>A função alerta recebe o código da resposta http, a URL e uma etapa. A função alerta vai gerar uma notificação de Windows com o estatus da conexão do API</p>
 
```
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
```

<h3>Tratamento do dados</h3>

<p>Para verificar as informações dos dados se usa <code>df.info()</code> e para visualizar os 5 primeiros valores ou os 5 últimos, se usaram <code>df.head(5) ou df.tail(5)</code>. O seguinte foi verificado</p>

<ul>
  <li>Valores nulos</li>
  <li>Colunas com campos combinados</li>
  <li>Caracteres especiais</li>
  <li>Remover acento</li>
  <li>Colunas com datas</li>
  <li>Eliminação de colunas</li>
</ul>



