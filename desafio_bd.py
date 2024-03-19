import sqlite3

# Classes da API
from classes_api import Cliente, Conta

def main():
  # Conexão com o Banco de Dados
  conexao = conectar_banco_dados()

  if conexao:
    # Menu Principal
    while True:
      print("\n\t\tGerenciamento de Clientes e Contas")
      print("=====================================")
      print("1. Clientes")
      print("2. Contas")
      print("0. Sair")

      opcao = input("\nDigite a sua opção: ")

      if opcao == "1":
        menu_clientes(conexao)
      elif opcao == "2":
        menu_contas(conexao)
      elif opcao == "0":
        break
      else:
        print("\nOpção inválida!")

    # Fechar Conexão com o Banco de Dados
    conexao.close()
  else:
    print("\nErro ao conectar com o banco de dados!")

if __name__ == "__main__":
  main()

def menu_clientes(conexao):
  while True:
    print("\n\t\tMenu de Clientes")
    print("=====================")
    print("1. Listar Clientes")
    print("2. Cadastrar Cliente")
    print("3. Ler Cliente")
    print("4. Atualizar Cliente")
    print("5. Deletar Cliente")
    print("0. Voltar")

    opcao = input("\nDigite a sua opção: ")

    if opcao == "1":
      listar_clientes(conexao)
    elif opcao == "2":
      cadastrar_cliente(conexao)
    elif opcao == "3":
      ler_cliente_por_id(conexao)
    elif opcao == "4":
      atualizar_cliente(conexao)
    elif opcao == "5":
      deletar_cliente(conexao)
    elif opcao == "0":
      break
    else:
      print("\nOpção inválida!")

def listar_clientes(conexao):
  cursor = conexao.cursor()
  comando = "SELECT * FROM cliente"
  cursor.execute(comando)
  resultado = cursor.fetchall()

  for cliente in resultado:
    cliente_objeto = Cliente(cliente[0], cliente[1], cliente[2], cliente[3])
    print(cliente_objeto)

def cadastrar_cliente(conexao):
  nome = input("Nome: ")
  cpf = input("CPF: ")
  endereco = input("Endereço: ")

  if criar_cliente(nome, cpf, endereco):
    print("\nCliente cadastrado com sucesso!")
  else:
    print("\nFalha ao cadastrar cliente!")

def ler_cliente_por_id(conexao):
  id_cliente = int(input("ID do Cliente: "))
  cliente = ler_cliente(id_cliente)

  if cliente:
    print(cliente)
  else:
    print("\nCliente não encontrado!")

def atualizar_cliente(conexao):
  id_cliente = int(input("ID do Cliente: "))
  nome = input("Novo Nome: ")
  cpf = input("Novo CPF: ")
  endereco = input("Novo Endereço: ")

  if atualizar_cliente(id_cliente, nome, cpf, endereco):
    print("\nCliente atualizado com sucesso!")
  else:
    print("\nFalha ao atualizar cliente!")

def deletar_cliente(conexao):
  id_cliente = int(input("ID do Cliente: "))

  if deletar_cliente(id_cliente):
    print("\nCliente deletado com sucesso!")
  else:
    print("\nFalha ao deletar cliente!")

def menu_contas(conexao):
  while True:
    print("\n\t\tMenu de Contas")
    print("=====================")
    print("1. Listar Contas")
    print("2. Cadastrar Conta")
    print("0. Voltar")

    opcao = input("\nDigite a sua opção: ")

    if opcao == "1":
      listar_contas(conexao)
    elif opcao == "2":
      cadastrar_conta(conexao)