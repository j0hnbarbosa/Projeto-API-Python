from src.CRUD.crud import cadastrarCliente
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def criaCliente():
  cadastrarCliente(request.json)
  print('VALOR Aqui {}'.format(request.json))
  return jsonify(request.json)

#Quando estiver usando o app.run(debug=True) execute usando 'python app.py'
if __name__ == '__main__':
  app.run(debug=True)