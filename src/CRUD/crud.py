from src.conexao.conexao import conectaDB

mydb = conectaDB()
mycursor = mydb.cursor()

print(mydb)


# Cria base de dados caso nao exista
def criaBases():
  try:
      mycursor.execute("Create DATABASE traba_db")
      tbl_cliente()
      tbl_veiculo()
      tbl_dono_veiculo()
      print("Database Criada Com sucesso!")
  except:
    print("Database já existe!") 


def tbl_cliente():
  try:
    mycursor.execute(
      "CREATE TABLE `traba_db`.`tbl_cliente` ( `id` INT NOT NULL AUTO_INCREMENT , `nome` VARCHAR(60) NOT NULL , `sobrenome` VARCHAR(60) NOT NULL , `endereco` VARCHAR(100) NOT NULL , `telefone` VARCHAR(15) NOT NULL , `cpf` VARCHAR(11) NOT NULL , PRIMARY KEY (`id`)) "
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


try:
  def cadastrarCliente(clienteNovo):

    nome, sobrenome, endereco, telefone, cpf = list(clienteNovo.values())
    sql = "INSERT INTO `traba_db`.`tbl_cliente` (`nome`, `sobrenome`, `endereco`, `telefone`, `cpf`) VALUES(%s, %s, %s, %s, %s)"
    vlr = (nome, sobrenome, endereco, telefone, cpf)
    print("clienteNovo: {}".format(vlr))

    mycursor.execute(sql, vlr)
    terminaConexao()

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')

try:
  def cadastrarVeiculo(veiculoNovo):
    marca, fabricante, ano, chassis, cor = list(veiculoNovo.values())
    sql = "INSERT INTO `traba_db`.`tbl_veiculo` (`marca`, `fabricante`, `ano`, `chassis`, `cor`) VALUES(%s, %s, %s, %s, %s)"
    vlr = (marca, fabricante, ano, chassis, cor)

    mycursor.execute(sql, vlr)

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')

try:
  def cadastrarDonoVeiculo(donoVeiculoNovo):
    idCliente, idViculo = list(donoVeiculoNovo.values())
    sql = "INSERT INTO `traba_db`.`tbl_dono_veiculo` (`idCliente`, `idVeiculo`) VALUES(%s, %s)"
    vlr = (idCliente, idViculo)

    mycursor.execute(sql, vlr)

    print("Dados criados com sucesso")
except:
  print('Dados não inseridos')



# donoVeiculoNovo = {}
# donoVeiculoNovo['idCliente'] = 14
# donoVeiculoNovo['idVeiculo'] = 1
# cadastrarDonoVeiculo(donoVeiculoNovo)

def terminaConexao():
  mydb.commit()
  # mydb.close()