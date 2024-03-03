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
**([functionsjv.py](https://github.com/JavoroG/Projeto_Final_Coder/blob/main/functionsjv.py))**

<h3>Arquivos do projeto:</h3>
<ul>
  <li>
    <strong><a href = "https://github.com/JavoroG/Projeto_Final_Coder/blob/main/functionsjv.py">functionsjv.py</a></strong><p>Contém as funções que permitem criar a base de estados, realizar o tratamento das bases, salvar no formato .csv e criar as tabelas.</p>
  </li> 
  <li>
    <strong>validar.py</strong> <p>Contém a função que valida se a conexão das URLs (APIs, HTML) foi bem-sucedida ou não e gera um alerta do Windows com os comentários.</p>
  </li>
  <li>
    <strong>reqhtml.py</strong> <p>Contém uma função que extrai uma tabela no formato HTML, armazena os dados numa lista e retorna um dataframe com esses dados.</p>
  </li>
  <li>
    <strong>requirements.txt</strong> <p>Contém as bibliotecas com suas respectivas versões utilizadas no projeto.</p>
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

<h3>Arquivos do projeto</h3>



<hr>
