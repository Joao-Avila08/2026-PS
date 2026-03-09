# Arquivo: 01b-debug.py

# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do aluno: ")#input é com N e nao com M

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2 #faltou os parenteses em volta do nota1+nota2 antes da divisao pra q a multiplicação antes da divisao

if media >= 6.0:
    situacao = "Aprovado"

elif media >= 4.0:
    situacao = "Recuperação"
else:#o else tava com identação errada
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")#o certo é print e nao pront