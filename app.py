from src.CRUD.crud import cadastrarCliente, criaBases, verificaLogin, cadastrarUsuario, recuperarSenha_verificaEmail
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

criaBases()

@app.route('/cadastrarCliente', methods=['POST'])
def cadastraCliente():
  cadastrarCliente(request.json)
  print('VALOR Aqui {}'.format(request.json))
  return jsonify(request.json)

@app.route('/login', methods=['GET', 'POST'])
def login():
  verificaLogin(request.json)
  return 'sucesso'

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastraUsuario():
  cadastrarUsuario(request.json)
  return 'sucesso - cadastrarUsuario'

@app.route('/recuperarSenhaVerificaEmail', methods=['GET'])
def recuperarSenhaVerificaEmail():
  recuperarSenha_verificaEmail(request.json)
  return 'sucesso - recuperarSenhaVerificaEmail'

#Quando estiver usando o app.run(debug=True) execute usando 'python app.py'
if __name__ == '__main__':
  app.run(debug=True)