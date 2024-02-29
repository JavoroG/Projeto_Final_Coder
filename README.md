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

<h3 >Bibliotecas utilizadas:</h3>
<ul>
<li>pandas</li>
<li>bs4</li>
<li>sqlite3</li>
<li>requests</li>
<li>datetime</li>
<li>plyer</li>
</ul>

<h3>Arquivos do projeto:</h3>
<ul>
  <li>functionsjv.py</li>
  <li>validar.py</li>
  <li>reqhtml.py</li>
</ul>
