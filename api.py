# -*- coding: utf-8 -*-

import flask
from flask import request, jsonify
import flask_api
from flask_api import status
import requests
import utils
from utils import ConverterFparaC

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API de temperaturas</h1>'''


@app.route('/converter-farenheint-para-celsius',methods =['POST'])
def FarenheitToCelsius():
    data = request.get_json() or {}
    if 'temperatura' not in data:
        content = {'Erro!': 'Não há temperatura a converter'}
        return content, status.HTTP_400_BAD_REQUEST

    temperatura = data['temperatura']
    temperaturaConvertida = ConverterFparaC(temperatura)
    return jsonify(f'Sua temperatura {temperatura}ºF convertida para Celsius é de: {temperaturaConvertida}ºC' ) 

@app.route('/api/forecast',methods =['POST'])
def BuscaDadosCidade():
    data = request.get_json() or {}
    if 'cidade' not in data:
        content = {'Erro!': 'Não há cidade a consultar'}
        return content, status.HTTP_400_BAD_REQUEST
    cidade = data['cidade']
    retornoApi= ConsultaApi(cidade)
    return jsonify(retornoApi) 

def ConsultaApi(cidade):
    payload ={'q': cidade, 'appid':'439d4b804bc8187953eb36d2a8c26a02' }
    r = requests.get("https://samples.openweathermap.org/data/2.5/weather?", params=payload)
    return r.json()

@app.route('/api/forecast',methods=['GET'])
def BuscaDadosCidadeGet():
    if 'city' in request.args:
        cidade = request.args['city']
        return ConsultaApi(cidade)
    else:
        content = {'Erro!': 'Não há cidade a consultar'}
        return content, status.HTTP_400_BAD_REQUEST       
    return jsonify('not implementeded')

app.run()
