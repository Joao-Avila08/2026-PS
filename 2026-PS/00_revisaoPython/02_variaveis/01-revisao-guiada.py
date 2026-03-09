#======================================================
# SISTEMA DE CONTROLE DE ESTOQUE
#======================================================
# Disciplina : Programação de Sistemas (PS)
# Autor      : João Vitor Gracietti De Ávila
# Data       : 03/03/2026
# Repositório: https://github.com/Joao-Avila08/2026-PS
#======================================================
# DESCRIÇÃO:
# Programa para processar produtos e quantidades.
# Determina a situação (Crítico, Adequado ou Excesso).
#======================================================

#dados do estoque
estoque = [
    {"produto": "Teclado", "quantidade": 3},
    {"produto": "Mouse", "quantidade": 10},
    {"produto": "Monitor", "quantidade": 25},
]

#uso de while
while True:
    print("\n=== Menu de Estoque ===")
    print ("1 - Mostrar todos os produtos (Relatório)")
    print("2 - Adicionar novo produto")
    print ("3 - Sair")

    opcao =input("Escolha uma opção: ")

    if opcao == "1":
        print ("\n=== RELATÓRIO GERAL ===")
        
        # variáveis para o resumo
        critico = 0
        adequado =0
        excesso = 0

        # percorre a lista para mostrar um por um 
        for item in estoque:
            nome = item["produto"]
            qtd =item["quantidade"]

            if qtd < 5:
                situacao = "Crítico"
                critico = critico + 1
            elif qtd <=20:
                situacao ="Adequado"
                adequado = adequado + 1
            else:
                situacao ="Excesso"
                excesso = excesso + 1

            print ("Produto  :", nome)
            print("Estoque  :", qtd)
            print("Situação :", situacao)
            print ("-" * 20)
        
        # exibe o resumo solicitado 
        print ("RESUMO -> Crítico:", critico, "| Adequado:", adequado, "| Excesso:", excesso)

    elif opcao =="2":
        nome_novo =input("Digite o nome do produto: ")
        qtd_nova = int(input("Digite a quantidade: "))

        if qtd_nova >=0:
            # cria o dicionário do novo produto
            novo = {"produto": nome_novo, "quantidade": qtd_nova}
            
            # adiciona na lista usando SOMA
            estoque = estoque + [novo]
            print ("✅ Produto adicionado!")
        else:
            print("❌ Erro: Quantidade negativa não permitida.")

    elif opcao == "3":
        # antes de fechar, mostra o menor estoque
        if len (estoque) > 0:
            menor_item = estoque[0]
            for item in estoque:
                if item["quantidade"] < menor_item["quantidade"]:
                    menor_item = item
            
            print("\nO item com menor estoque é:", menor_item["produto"])
            print ("Quantidade:", menor_item["quantidade"])
            
        print ("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")