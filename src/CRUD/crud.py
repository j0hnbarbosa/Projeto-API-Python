from src.conexao.conexao import conectaDB

mydb = conectaDB()
mycursor = mydb.cursor()

print(mydb)


# ========= Cria base de dados caso nao exista =================
def criaBases():
  try:
      mycursor.execute("create DATABASE traba_db")
      tbl_usuario()
      tbl_cliente()
      tbl_veiculo()
      tbl_dono_veiculo()
      print("Database Criada Com sucesso!")
      # terminaConexao()
  except:
    print("Database já existe!") 


def tbl_cliente():
  try:
    mycursor.execute(
      "CREATE TABLE `traba_db`.`tbl_cliente` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `sobrenome` VARCHAR(60) NOT NULL , `endereco` VARCHAR(100) NOT NULL , `telefone` VARCHAR(15) NOT NULL , `cpf` VARCHAR(11) NOT NULL, `email` VARCHAR(60) NOT NULL, `senha` VARCHAR(60) NOT NULL, PRIMARY KEY (`id`)) "
      )
    print('Tabela criada com sucess!')
  except:
    print("Tabela já criada.")

def tbl_veiculo():
  try:
    mycursor.execute(
      "CREATE TABLE `traba_db`.`tbl_veiculo` ( `id` INT NOT NULL AUTO_INCREMENT , `marca` VARCHAR(60) NOT NULL , `fabricante` VARCHAR(60) NOT NULL , `ano` DATE NOT NULL , `chassis` VARCHAR(60) NOT NULL , `cor` VARCHAR(60) NOT NULL , PRIMARY KEY (`id`))"
      )
    print('Tabela criada com sucess!')
  except:
    print("Tabela já criada.")

def tbl_dono_veiculo():
  try:
    mycursor.execute(
      "CREATE TABLE `traba_db`.`tbl_dono_veiculo` ( `id` INT NOT NULL AUTO_INCREMENT , `marca` VARCHAR(60) NOT NULL , `fabricante` VARCHAR(60) NOT NULL , `ano` DATE NOT NULL , `chassis` VARCHAR(60) NOT NULL , `cor` VARCHAR(60) NOT NULL , PRIMARY KEY (`id`))"
      )
    print('Tabela criada com sucess!')
  except:
    print("Tabela já criada.")

def tbl_usuario():
  try:
    mycursor.execute(
      "CREATE TABLE `traba_db`.`tbl_usuario` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `email` VARCHAR(60) NOT NULL , `senha` VARCHAR(60) NOT NULL , PRIMARY KEY (`id`))"
      )
    print('Tabela criada com sucess!')
  except:
    print("Tabela já criada.")

# ========= Manipula as tabelas =================

try:
  def cadastrarCliente(valores):

    sql = "INSERT INTO `traba_db`.`tbl_cliente` (`nome`, `sobrenome`, `endereco`, `telefone`, `cpf`, `email`, `senha`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    vlr = (valores['nome'], valores['sobrenome'], valores['endereco'], valores['telefone'], valores['cpf'], valores['email'], valores['senha'])
    print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')

try:
  def cadastrarVeiculos(valores):

    sql = "INSERT INTO `traba_db`.`tbl_veiculo` (`marca`, `fabricante`, `ano`, `chassis`, `cor`) VALUES(%s, %s, %s, %s, %s)"
    vlr = (valores['marca'], valores['fabricante'], valores['ano'], valores['chassis'], valores['cor'])
    print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')

try:
  def cadastrarDonoVeiculo(valores):
    idCliente, idViculo = list(valores.values())
    sql = "INSERT INTO `traba_db`.`tbl_dono_veiculo` (`idCliente`, `idVeiculo`) VALUES(%s, %s)"
    vlr = (idCliente, idViculo)

    mycursor.execute(sql, vlr)
    terminaConexao()

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')

try:
  def verificaLogin(valores):
    sql = "SELECT * from `traba_db`.`tbl_usuario` where email=%s and senha=%s"
    vlr = (valores['email'], valores['senha'])
    mycursor.execute(sql, vlr)
    # print("Valores da base {}".format(mycursor.fetchone()))
    # resu = mycursor.fetchone()
    print(mycursor.fetchone())
    terminaConexao()
    return 'sucesso'
except:
  print('Dados não inseridos')

try:
  def cadastrarUsuario(valores):
    sql = "INSERT INTO `traba_db`.`tbl_usuario` (`nome`, `email`, `senha`) VALUES (%s, %s, %s)"
    vlr = (valores['nome'], valores['email'], valores['senha'])
    print("Valores da base {}".format(vlr))
    mycursor.execute(sql, vlr)
    terminaConexao()
except:
  print('Dados não inseridos')

try:
  def trocarSenha(valores):
    sql = "UPDATE `traba_db`.`tbl_usuario` SET senha=%s where id=%s"
    vlr = (valores['nome'], valores['email'], valores['senha'])
    print("Valores da base {}".format(vlr))
    mycursor.execute(sql, vlr)
    terminaConexao()
except:
  print('Dados não inseridos')

try:
  def recuperarSenha_verificaEmail(valores):
    
    print("valores {}".format(valores['email']))
    sql = "SELECT * from `traba_db`.`tbl_usuario` where 1=1 and email='{}'".format(valores['email'])
    print(sql)
    mycursor.execute(sql)
    resu = mycursor.fetchone()
    terminaConexao()    
    return resu
except:
  print('Dados não inseridos')


try:
  def listarClientes():
    
    sql = "SELECT * from `traba_db`.`tbl_cliente` where 1=1"
    # print(sql)
    mycursor.execute(sql)
    resu = mycursor.fetchall()
    terminaConexao()
    resuThat = []
    field_names = [i[0] for i in mycursor.description]
    for l in resu:
      temp = {}
      for index, j in enumerate(l):
        temp[field_names[index]] = j
      resuThat.append(temp)
    
    print(resuThat)

    return resuThat
except:
  print('Dados não inseridos')


try:
  def listarVeiculos():
    sql = "SELECT * from `traba_db`.`tbl_veiculo` where 1=1"
    # print(sql)
    mycursor.execute(sql)
    resu = mycursor.fetchall()
    terminaConexao()
    resuThat = []
    
    field_names = [i[0] for i in mycursor.description]

    for l in resu:
      temp = {}
      for index, j in enumerate(l):
        temp[field_names[index]] = j
      resuThat.append(temp)
    
    print(resuThat)

    return resuThat
except:
  print('Dados não inseridos')

try:
  def deletarCliente(valores):
    print(valores)
    sql = "DELETE from `traba_db`.`tbl_cliente` where id={0}".format(valores['id'])
    # vlr = (valores['id'])
    mycursor.execute(sql)
    terminaConexao()
except:
  print("Dados apagados!")
  
try:
  def deletarVeiculo(valores):
    print(valores)
    sql = "DELETE from `traba_db`.`tbl_veiculo` where id={0}".format(valores['id'])
    # vlr = (valores['id'])
    mycursor.execute(sql)
    terminaConexao()
except:
  print("Dados apagados!")


def editarCliente(valores, id):
  print(valores)
  try:
    sql = "UPDATE `traba_db`.`tbl_cliente` SET `nome`=%s, `sobrenome`=%s, `endereco`=%s, `telefone`=%s, `cpf`=%s, `email`=%s, `senha`=%s where id=%s"
    vlr = (valores['nome'], valores['sobrenome'], valores['endereco'], valores['telefone'], valores['cpf'], valores['email'], valores['senha'], int(id))
    # sql = "UPDATE `traba_db`.`tbl_cliente` SET `nome`=%s where id=%s"
    # vlr = (valores['nome'], valores['id'])
    # print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()
    return "sucesso"

  except:
    print("ERRO na EDICAO.")
    return "ERRO na EDICAO."

def editarVeiculo(valores, id):
  print(valores)
  try:
    sql = "UPDATE `tbl_veiculo` SET `marca` = %s, `fabricante` = %s, `ano` = %s, `chassis` = %s, `cor` = %s WHERE `tbl_veiculo`.`id` = %s"
    vlr = (valores['marca'], valores['fabricante'], valores['ano'], valores['chassis'], valores['cor'], int(id))
    # sql = "UPDATE `traba_db`.`tbl_cliente` SET `nome`=%s where id=%s"
    # vlr = (valores['nome'], valores['id'])
    # print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()
    return "sucesso"

  except:
    print("ERRO na EDICAO.")
    return "ERRO na EDICAO."

# donoVeiculoNovo = {}
# donoVeiculoNovo['idCliente'] = 14
# donoVeiculoNovo['idVeiculo'] = 1
# cadastrarDonoVeiculo(donoVeiculoNovo)

def terminaConexao():
  mydb.commit()
  # mydb.close()