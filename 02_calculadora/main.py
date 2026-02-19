def entrada():
    A=int(input("Digite 1 valor:"))
    B=int(input("Digite outro valor:"))
    op=input("Digite a Operação[* / + -]:")
    msg = f'{A} {op} {B}'

    if op ==  '+':
        res = Soma(A,B)
    elif op == '-':
        res=Subtração(A,B)
    elif op == '*':
        res=Multiplicação(A,B)
    elif op == '/':
        res=Divisao(A,B)
    Saida(msg,res)

def Soma(A,B):
    return(A+B)
  
def Subtração(A,B):
    return(A-B)
    
def Multiplicação(A,B):
    return(A*B)

def Divisao(A,B):
    return(A/B)

def Saida(msg, resultado):
    print(f"{msg} = {resultado}")
entrada()
