#======================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS
#======================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : João Vitor Gracietti De Ávila
# Data       : 24/02/2026
# Repositório: https://github.com/Joao-Avila08/2026-PS
#======================================================
#
# DESCRIÇÃO:
# Este programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.
#======================================================

# ---- DADOS DA TURMA ----
# Uma lista de dicionários: cada dicionário representa um aluno

turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
]

print("=== Resultado da Turma ===")
print()

# ---- PROCESSAMENTO COM FOR ----
for aluno in turma:

    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]

    media = (nota1 + nota2) / 2

    if media >= 6.0:
        situacao = "✅ Aprovado"
    elif media >= 4.0:
        situacao = "⚠️ Recuperação"
    else:
        situacao = "❌ Reprovado"

    print(f"Aluno   : {nome}")
    print(f"Média   : {media:.2f}")
    print(f"Situação: {situacao}")

    if nota1 < 2.0 or nota2 < 2.0:
        print("⚠️ Atenção: nota muito baixa em uma das avaliações.")

    print("-" * 30)


# ---- MENU COM WHILE ----
while True:
    print("\n=== Menu ===")
    print("1 - Adicionar novo aluno")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))

        media = (nota1 + nota2) / 2

        if media >= 6.0:
            situacao = "✅ Aprovado"
        elif media >= 4.0:
            situacao = "⚠️ Recuperação"
        else:
            situacao = "❌ Reprovado"

        print(f"\nAluno   : {nome}")
        print(f"Média   : {media:.2f}")
        print(f"Situação: {situacao}")

        if nota1 < 2.0 or nota2 < 2.0:
            print("⚠️ Atenção: nota muito baixa em uma das avaliações.")

    elif opcao == "2":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")