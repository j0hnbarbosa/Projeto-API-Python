from src.CRUD.crud import cadastrarCliente, criaBases, verificaLogin, cadastrarUsuario, recuperarSenha_verificaEmail, trocarSenha
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# criaBases()

@app.route('/cadastrarCliente', methods=['POST'])
def cadastraCliente():
  cadastrarCliente(request.json)
  print('VALOR Aqui {}'.format(request.json))
  return jsonify(request.json)

@app.route('/login', methods=['GET', 'POST'])
def login():
  resu = verificaLogin(request.json)
  print(resu)
  return  resu if resu != None else "ERRO"

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastraUsuario():
  cadastrarUsuario(request.json)
  return 'sucesso - cadastrarUsuario'

@app.route('/trocarSenha', methods=['GET'])
def trocaSenha():
  trocarSenha(request.json)
  return 'sucesso'

@app.route('/recuperarSenhaVerificaEmail', methods=['GET'])
def recuperarSenhaVerificaEmail():
  recuperarSenha_verificaEmail(request.json)
  return jsonify(recuperarSenha_verificaEmail(request.json))

@app.route('/cadastrarVeiculo', methods=['POST'])
def cadastrarVeiculo():
  
  return 'TEste cadastrarVeiculo'

@app.route('/listarCliente', methods=['GET'])
def listarCliente():
  return 'TEste listarCliente'

@app.route('/listarVeiculo', methods=['GET'])
def listarVeiculo():
  
  return 'TEste listarVeiculo'

@app.route('/editarCliente', methods=['PUT'])
def editarCliente():
  return 'TEste editarCliente'

@app.route('/editarVeiculo', methods=['PUT'])
def editarVeiculo():
  return 'TEste editarVeiculo'


#Quando estiver usando o app.run(debug=True) execute usando 'python app.py'
if __name__ == '__main__':
  app.run(debug=True)