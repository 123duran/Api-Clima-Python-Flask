 ### API em python usando Flask
 
 ### Objetivo da API
 Essa APi tem por objetivo retornar informações obtidas de uma API externa, ou seja, implementa uma integração com uma API de terceiros.
 Também é possível utilizar a API para converter Temperaturas em Farenheit para Celsius.

 ### Requerimentos

 - Pip
 - Flask
 - Pytest

 ### Instalação dos requerimentos
 ```sh
$ pip istall flask
$ pip istall flask-api
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