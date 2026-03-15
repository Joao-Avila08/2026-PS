# Arquivo: 01b-debug.py

# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem   # ERRO 1: faltava return. A função criava a mensagem mas não devolvia.

print(saudacao("Ana"))
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2
    return resultado   # ERRO 2: faltava return. Sem isso a função retornava None.

print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    global total   # ERRO 3: precisava declarar global para modificar a variavel fora da funcao
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n):

    if n < 0:   # ERRO 4: faltava caso base da recursao, sem isso geraria RecursionError
        return

    print(n)
    contagem(n - 1)

contagem(3)