# coding: utf-8

from flask import Flask, request

app = Flask(__name__)

'''Adiciona o callback da requisição antes do dado '''
def insert_callback(data):
    try:
        return "{0}({1})".format(request.args['callback'],data)
    except:
        return "{0}({1})".format('not callback' ,data)

''' Rota para renderizar a página inicial da aplicação'''
@app.route('/', methods=['GET'])
def all():
    tanque = request.args.get('tanque')
    gramas = request.args.get('gramas')
    return insert_callback("OK")

'''__main__'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)