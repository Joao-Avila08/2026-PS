#==================================================
# SISTEMA DE CONTROLE DE ESTOQUE
# Disciplina: Programação de Sistemas
# Aluno: João Vitor Gracietti De Ávila
# Data: 03/03/2026
# Descrição: Programa para controle de estoque
#==================================================

produtos = [
    ["Teclado", 3],
    ["Mouse", 10],
    ["Monitor", 25]
]

def mostrar_relatorio():
    critico = 0
    adequado = 0
    excesso = 0

    print("\n===== RELATÓRIO DE ESTOQUE =====\n")
    for produto in produtos:
        nome = produto[0]
        quantidade = produto[1]

        if quantidade < 5:
            situacao = "Crítico"
            critico += 1
        elif quantidade <= 20:
            situacao = "Adequado"
            adequado += 1
        else:
            situacao = "Excesso"
            excesso += 1

        print(f"Produto: {nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Situação: {situacao}")
        print("----------------------------")

    print("\nResumo geral")
    print(f"Crítico: {critico}")
    print(f"Adequado: {adequado}")
    print(f"Excesso: {excesso}")
    print("==============================\n")

def consultar_produto():
    while True:
        nome_busca = input("Digite o nome do produto para consultar (ou 'n' para sair): ").strip().lower()
        if nome_busca == "n":
            break

        encontrado = False
        for produto in produtos:
            if produto[0].lower() == nome_busca:
                print(f"Produto encontrado - {produto[0]} | Quantidade: {produto[1]}")
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado.")

        resp = input("Deseja consultar outro produto? (s/n): ").strip().lower()
        if resp != "s":
            break

def adicionar_produto():
    while True:
        nome_novo = input("Digite o nome do novo produto (ou 'n' para sair): ").strip()
        if nome_novo.lower() == "n":
            break

        try:
            quantidade_nova = int(input("Digite a quantidade: "))
            if quantidade_nova < 0:
                print("Quantidade não pode ser negativa.")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        # Verifica se produto já existe
        existe = False
        for produto in produtos:
            if produto[0].lower() == nome_novo.lower():
                print(f"{produto[0]} já existe. Atualizando quantidade...")
                produto[1] += quantidade_nova
                existe = True
                break

        if not existe:
            produtos.append([nome_novo, quantidade_nova])
            print("Produto adicionado.")

        resp = input("Deseja adicionar outro produto? (s/n): ").strip().lower()
        if resp != "s":
            break

def produto_menor_estoque():
    if produtos:
        menor = produtos[0]
        for produto in produtos:
            if produto[1] < menor[1]:
                menor = produto
        print(f"\nProduto com menor estoque: {menor[0]} - {menor[1]} unidades\n")

# ======== MENU PRINCIPAL ========
while True:
    print("=== SISTEMA DE ESTOQUE ===")
    print("1 - Mostrar relatório")
    print("2 - Consultar produto")
    print("3 - Adicionar produto")
    print("4 - Produto com menor estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        mostrar_relatorio()
    elif opcao == "2":
        consultar_produto()
    elif opcao == "3":
        adicionar_produto()
    elif opcao == "4":
        produto_menor_estoque()
    elif opcao == "5":
        print("Fim do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")