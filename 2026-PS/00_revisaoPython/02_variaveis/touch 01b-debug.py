# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contem 4 erros propositais. Encontre e corrija todos!

nome =  input("Digite o nome do aluno: ")
notal = float (input ("Digite a nota 1: ") )
nota2 = float (input ("Digite a nota 2: ") )

media = (notal + nota2)/2

if media >= 6.0:

    situacao = "Aprovado"
elif media >= 4.0:

    situacao = "Recuperação"

else:

    situacao = "Reprovado"

print (f"Aluno: {nome} | Media: {media: .2f} | Situacao: {situacao}")