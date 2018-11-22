from flask import Flask, request

app = Flask(__name__)

''' Rota para renderizar a página inicial da aplicação'''
@app.route('/', methods=['GET'])
def all():
    tanque = request.args.get('tanque')
    gramas = request.args.get('gramas')
    return "OK"

'''__main__'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)