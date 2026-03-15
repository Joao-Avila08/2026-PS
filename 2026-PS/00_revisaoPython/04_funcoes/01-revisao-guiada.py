#===============================================
#SISTEMA DE CALCULO DE IMC
#===============================================
#Disciplina : programacao de Sistema(PS)
#Aula       : 06 - revisao: funcoes
#autor      : Joao Vitor Gracietti De Avila
#data       : 03/03/26
#Repositorio:https://github.com/Joao-Avila08/2026-PS.git
#===============================================
# DESCRICAO:
#
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definicao de funcoes, parametros,
# retorno, escopo e recursao.
#
# ===============================================

# ---- FUNCAO SEM PARAMETROS E SEM RETORNO ----

def exibir_cabecalho():
    """Exibe o cabecalho do sistema no terminal."""

    print("=" * 40)
    print("  SISTEMA DE CALCULO DE IMC")
    print("=" * 40)


def exibir_rodape():
    print("=" * 40)
    print("Sistema encerrado.")
    print("=" * 40)


# Chamando a funcao
exibir_cabecalho()

# ---- FUNCAO COM PARAMETROS E RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Formula: peso / altura²"""
    imc = peso / (altura ** 2)
    return imc

# Coletando dados do usuario
peso   = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Chamando a funcao e armazenando o retorno
resultado = calcular_imc(peso, altura)

print(f"Seu IMC e: {resultado:.2f}")

# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"

def demonstrar_escopo():

    mensagem = "Ola do interior da funcao"

    print("Dentro da funcao:")

    print(f"  mensagem = {mensagem}")
    print(f"  versao   = {versao}")

demonstrar_escopo()

print("\nFora da funcao:")

print(f"  versao = {versao}")
# print(mensagem)


# FUNCAO pedida na atividade
def mostrar_versao():
    print(f"Sistema IMC - versao {versao}")

mostrar_versao()


# ---- VALOR PADRAO E MULTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificacao e emoji de status."""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"

    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"

    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"

    else:
        classificacao = "Obesidade"
        emoji = "🔴"

    return classificacao, emoji


# Chamada sem o parametro opcional
imc_teste = 22.5

classificacao, emoji = classificar_imc(imc_teste)

print(f"IMC {imc_teste} ({classificacao}) {emoji}")


# Chamada informando o parametro opcional
classificacao, emoji = classificar_imc(imc_teste, unidade="lb/in²")

print(f"Mesma chamada com unidade customizada: {classificacao} {emoji}")


# ---- RECURSAO BASICA ----

def contagem_regressiva(n):

    if n < 0:
        return

    print(n)
    contagem_regressiva(n - 1)


print("\n--- Contagem regressiva ---")
contagem_regressiva(5)


# Fatorial

def fatorial(n):

    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)


print("\n--- Fatorial ---")
for i in range(1, 7):
    print(f" {i}! = {fatorial(i)}")


# FUNCAO pedida na atividade
def soma_regressiva(n):

    if n == 1:
        return 1

    return n + soma_regressiva(n - 1)


print("\n--- Soma regressiva ---")
print(soma_regressiva(4))


# ----- FUNCAO PRINCIPAL -----

def processar_pessoa():
    
    nome   = input("\nNome: ")
    peso   = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)

    classificacao, emoji = classificar_imc(imc)

    print("\n--- Resultado ---")
    print(f"Nome           : {nome}")
    print(f"IMC            : {imc:.2f} kg/m²")
    print(f"Classificacao  : {classificacao} {emoji}")


# ----- EXECUCAO PRINCIPAL -----

exibir_cabecalho()

continuar = "s"

while continuar == "s":
    processar_pessoa()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()

exibir_rodape()