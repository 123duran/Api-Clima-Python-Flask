 ### API em python usando Flask
 
 ### Objetivo da API
 Essa API tem por objetivo retornar informações obtidas de uma API externa (OpenWeatherMap), ou seja, implementa uma integração com uma API de terceiros.
 Também é possível utilizar a API para converter Temperaturas em Farenheit para Celsius.
 Testes unitários também foram criados utilizando o Pytest.

 ### Requerimentos
 - Python 3.8 ou mais recente
 - Pip
 - Flask
 - Pytest

 ### Instalação dos requerimentos
 Partimos do pressuposto que você já instalou o Python 3.8 e o Pip.
 Para verificar a versão do Python:
 ```sh
$ python -V
ou
$ python --version
```
Para verificar a versão do Pip:
```sh
$ pip -V
ou
$ pip --version
```
 Após instalar o PIP, devemos utilizá-lo para instalar as outras dependências do projeto.
 ```sh
$ pip install flask
$ pip install flask-api
$ pip install pytest pytest-html
```

### Rodando a API
Para rodarmos a api devemos executar o comando:
 ```sh
$ python api.py
```
Por padrão a API irá rodar em http://127.0.0.1:5000/

### Executando os testes unitários
Para exectutar os testes unitários executar o seguinte comando:
 ```sh
$ pytest
```
Será gerado um arquivo chamado report.html com o resultado dos testes ;)

