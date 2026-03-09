#======================================================
# SISTEMA DE CONTROLE DE ESTOQUE
#======================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisao: Estruturas de Dados
# Autor      : João Vitor Gracietti De Ávila
# Data       : 07/03/2026
# Repositório: https://github.com/Joao-Avila08/2026-PS
#======================================================
# DESCRIÇÃO:
# Catalogo de livros que demonstra o uso de 
# listas e dicionarios para armazenar, consultar e filtrar
# dados estruturados.
#======================================================
#---- LISTAS: CONCEITO BASICO ----

# criando uma lista de titulos
titulos = [
    "O programador pragmatico",
    "Codigo Limpo",
    "Entendendo Algoritimos"
]
#Acesso por indice (começa em 0, nao em 1)
print("Primeiro Livro:", titulos [0])
print("Ultimo livro:", titulos[-1])#Indice -1 = ultimo elemento
print("Total de livros", len(titulos))
#---- METODOS DE LISTA ----
print("\n--- Operaçoes na lista ---")

#adicionar um item no final
titulos.append("Python Fluente")
print("Apos append:", titulos)

#verifivar se um item existe
busca = "Codigo Limpo"
if busca in titulos:
    print(f'"{busca}" está no catalogo.')
else:
    print (f'"{busca}"nao encontrado.')

#Ordenar a lista
titulos.sort()
print("Lista Ordenada:", titulos)

#remover um item 
titulos.remove("Entendendo Algoritimos")
print ("Apos remove:", titulos)

# ---- DICIONAROS: CONCEITO BASICO ----

#um dicionario representa um livro com seus atributos
livro={
    "titulo":       "O programador pragmatico",
    "autor":        "Andrew Hunt",
    "ano":          "1999", #int, nao string
    "disponivel":   "True", #bool
}
#acessando valores pelas chaves
print("titulo  :", livro["titulo"])
print("Autor   :", livro["autor"])
print("Ano     :", livro["ano"])
print("Status  :", "Disponivel"if livro["disponivel"]else "Emprestado")

# ----MODIFICANDO E CONSULTANDO ----
#Atualizando um valor existente
livro["disponivel"]= False #lvro foi emprestado
print("\nApos emprestimo:", livro["disponivel"])

#adicionando uma nova chave
livro["paginas"] = 352
print("Paginas",livro["paginas"])

#.get() - acesso seguro: retorna None(ou padrao) se a chave nao existir
editora = livro.get("editora", "nao informada")
print("Editora", editora)#nao lança KeyError, retorna o padrao

# ---- CATALOGO: LISTA DE DICIONARIOS ----
catalogo =[
    {"titulo": "O programador pragmatico", "autor": "Andrew Hunt", "ano":1999, "disponivel":True},
    {"titulo": "Codigo Limpo", "autor": "Robert C. Martin", "ano": 2008,"disponivel": False},
    {"titulo": "Entendendo algoritimos", "autor": "Aditya Bhargava", "ano": 2016,"disponivel":True},
]
print("=== Catalogo da Biblioteca====")
print()

#Percorrendo cada livro com for
for livro in catalogo:
    status = "✅ Disponivel" if livro ["disponivel"] else "📕 Emprestado"
    print(f'{livro["titulo"]}({livro["ano"]})')
    print(f' Autor: {livro["autor"]} | {status}')
    print(" "+"-"*40)

# ---- CONSULTAS E FILTROS ----

print("\n=== Livros disponiveis ===")
for livro in catalogo:
    if livro["disponivel"]:        # filtra apenas os disponíveis
     print(f'  ✅ {livro["titulo"]}')
print("\n=== Busca por título ===")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro["titulo"].lower(): # .lower() ignora maiúsculas/minúsculas
        print(f'  Encontrado: {livro["titulo"]} — {livro["autor"]}')
        encontrado = True
if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")
print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():  # .items() retorna pares (chave, valor)
    print(f"  {chave}: {valor}")

