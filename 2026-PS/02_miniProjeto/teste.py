#=================================================#
#              PIZZARIA DOS BETINHA               #
#=================================================#
# Disciplina: Programação de Sistemas             
# Aula: Número 13                                 
# Data: 28/03/2025                                
# Autores: Bruno de Paula, João Ávila, João Mauda 
#=================================================#
# OBJETIVO:
# Sistema para gerenciar uma pizzaria, com controle
# de ingredientes, funcionários e vendas.
#=================================================#
# Cabeçalho completo com disciplina, aula, integrantes e descrição

from datetime import datetime
# Biblioteca usada para trabalhar com data e hora (usada no histórico)

# Variáveis com nomes significativos
ARQUIVO = "2026-PS/03_miniProjeto/dados.txt"
SEPARADOR = "|"
# Exemplo de uso no arquivo:
# ING|Queijo
# FUNC|João|Pizzaiolo|1500
# VENDA|50.0

#================ HISTÓRICO =================#

def registrar_historico(texto):
    # Função com responsabilidade específica (registrar ações)
    # Recebe parâmetro (texto)

    # Persistência em arquivo (.txt)
    with open("2026-PS/03_miniProjeto/historico.txt", "a", encoding="utf-8") as f:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        # Exemplo: 09/04/2026 14:30

        f.write(f"[{agora}] {texto}\n")
        # Exemplo:
        # [09/04/2026 14:30] Venda registrada: R$50

#================ FUNÇÕES =================#

def carregar_dados():
    # Função com retorno (return dados)
    # Usa múltiplos tipos de dados:
    # - lista (ingredientes, vendas)
    # - dicionário (funcionarios)
    # - float (valores numéricos)

    dados = {
        "ingredientes": [],
        "funcionarios": [],
        "vendas": []
    }

    try:
        # try/except para evitar erro se o arquivo não existir
        with open(ARQUIVO, "r", encoding="utf-8") as f: 
            for linha in f:
                # Estrutura de repetição (for)

                partes = linha.strip().split(SEPARADOR)
                # Exemplo:
                # "FUNC|João|Pizzaiolo|1500"
                # vira ["FUNC", "João", "Pizzaiolo", "1500"]

                # Estrutura de decisão
                if len(partes) < 2:
                    continue

                tipo, info = partes[0], partes[1:]

                # Operador relacional (==)
                if tipo == "ING":
                    dados["ingredientes"].append(info[0])

                elif tipo == "FUNC":
                    nome, funcao, salario = info
                    dados["funcionarios"].append({
                        "nome": nome,
                        "funcao": funcao,
                        "salario": float(salario)
                        # Converte string → número (float)
                    })

                elif tipo == "VENDA":
                    dados["vendas"].append(float(info[0]))

    except FileNotFoundError:
        # Permite executar o sistema mesmo sem dados.txt
        pass

    return dados


def salvar_dados(dados):
    # Função responsável por salvar dados (persistência)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        # Sobrescreve o arquivo com dados atualizados

        for ing in dados["ingredientes"]:
            f.write(f"ING{SEPARADOR}{ing}\n")

        for func in dados["funcionarios"]:
            f.write(f"FUNC{SEPARADOR}{func['nome']}{SEPARADOR}{func['funcao']}{SEPARADOR}{func['salario']}\n")

        for venda in dados["vendas"]:
            f.write(f"VENDA{SEPARADOR}{venda}\n")

#================ INGREDIENTES =================#

def listar_ingredientes(dados):
    print("\nIngredientes:")

    # Estrutura de decisão
    if not dados["ingredientes"]:
        print("Nenhum ingrediente cadastrado.")
        return

    # Estrutura de repetição (for)
    for i, ing in enumerate(dados["ingredientes"], 1):
        # Exemplo:
        # 1. Queijo
        print(f"{i}. {ing}")


def adicionar_ingrediente(dados):
    nome = input("Digite o nome do ingrediente: ")

    # Operadores lógicos (or) e relacionais (<)
    if not nome.strip() or len(nome) < 2:
        print("Nome inválido.")
        return

    # Operador relacional (in)
    if nome in dados["ingredientes"]:
        print("Ingrediente já existe.")
        return

    dados["ingredientes"].append(nome)
    salvar_dados(dados)
    registrar_historico(f"Ingrediente adicionado: {nome}")
    print("Ingrediente adicionado.")

#================ FUNCIONÁRIOS =================#

def listar_funcionarios(dados):
    print("\nFuncionários:")

    if not dados["funcionarios"]:
        print("Nenhum funcionário cadastrado.")
        return

    for f in dados["funcionarios"]:
        print(f"{f['nome']} - {f['funcao']} - R${f['salario']}")


def adicionar_funcionario(dados):
    nome = input("Nome: ")
    funcao = input("Cargo: ")

    # for + if (busca e validação)
    for f in dados["funcionarios"]:
        if f["nome"] == nome:
            print("Funcionário já cadastrado.")
            return

    try:
        # try/except para entrada do usuário
        salario = float(input("Salário: "))
    except ValueError:
        print("Salário invalido. Digite uma entrada aceita (apenas numeros)")
        return

    dados["funcionarios"].append({
        "nome": nome,
        "funcao": funcao,
        "salario": salario
    })

    salvar_dados(dados)
    registrar_historico(f"Funcionário adicionado: {nome}")
    print("Funcionário cadastrado.")

#================ VENDAS =================#

def registrar_venda(dados):
    try:
        valor = float(input("Valor da venda: "))
    except ValueError:
        print("Valor inválido.")
        return

    dados["vendas"].append(valor)
    salvar_dados(dados)
    registrar_historico(f"Venda registrada: R${valor}")
    print("Venda registrada.")


def relatorio(dados):
    # Operadores aritméticos
    total_vendas = sum(dados["vendas"])
    total_funcionarios = len(dados["funcionarios"])
    custo = total_funcionarios * 100
    lucro = total_vendas - custo

    print("\nRelatório do dia")
    print(f"Total de vendas: R${total_vendas}")
    print(f"Número de funcionários: {total_funcionarios}")
    print(f"Custo estimado: R${custo}")
    print(f"Lucro bruto: R${lucro}")

    # Estrutura de decisão
    if dados["vendas"]:
        print(f"Maior venda: R${max(dados['vendas'])}")
        print(f"Menor venda: R${min(dados['vendas'])}")
        print(f"Média: R${sum(dados['vendas'])/len(dados['vendas'])}")

#================ BUSCA =================#

def buscar_funcionario(dados):
    nome = input("Buscar funcionário: ")

    for f in dados["funcionarios"]:
        # Comparação de texto ignorando maiúsculas/minúsculas
        if nome.lower() in f["nome"].lower():
            print(f"{f['nome']} - {f['funcao']} - R${f['salario']}")

#================ MENU =================#

def menu():
    dados = carregar_dados()

    # Estrutura de repetição (while)
    while True:
        print("\nPIZZARIA DOS BETINHA")
        print("1 - Listar ingredientes")
        print("2 - Adicionar ingrediente")
        print("3 - Listar funcionários")
        print("4 - Adicionar funcionário")
        print("5 - Registrar venda")
        print("6 - Ver relatório")
        print("7 - Buscar funcionário")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        # Estrutura de decisão completa (if/elif/else)
        if escolha == "1":
            listar_ingredientes(dados)
        elif escolha == "2":
            adicionar_ingrediente(dados)
        elif escolha == "3":
            listar_funcionarios(dados)
        elif escolha == "4":
            adicionar_funcionario(dados)
        elif escolha == "5":
            registrar_venda(dados)
        elif escolha == "6":
            relatorio(dados)
        elif escolha == "7":
            buscar_funcionario(dados)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

#================ EXECUÇÃO =================#

# Garante que não há código solto fora de funções
# O programa começa aqui
if __name__ == "__main__":
    menu()