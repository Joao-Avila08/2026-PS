#======================================================
# SISTEMA DE BIBLIOTECA
#======================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisao: Estruturas de Dados
# Autor      : João Vitor Gracietti De Ávila
# Data       : 09/03/2026
# Repositório: https://github.com/Joao-Avila08/2026-PS
#======================================================
# DESCRICAO: Programa em Python que simula um sistema simples de biblioteca,
# permite visualizar o catalogo de livros, cadastrar novos livros,
# buscar livros por autor, registrar emprestimos e devolucoes
# e gerar um relatorio final com livros disponiveis e emprestados.

# catalogo inicial com 3 livros
catalogo = [
    {"titulo": "O programador pragmatico", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Codigo Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": False},
    {"titulo": "Entendendo algoritimos", "autor": "Aditya Bhargava", "ano": 2016, "disponivel": True},
]

# mostrar todos os livros
print("=== Catalogo da Biblioteca ===")
for livro in catalogo:
    status = "Disponivel" if livro["disponivel"] else "Emprestado"
    print(livro["titulo"], "-", livro["autor"], "|", status)

# cadastrar novo livro
print("\n=== Cadastro de novo livro ===")
titulo = input("Titulo: ")
autor = input("Autor: ")
ano = int(input("Ano: "))

# cria dicionario do livro
novo_livro = {
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "disponivel": True
}

# adiciona no catalogo
catalogo.append(novo_livro)
print("\nLivro cadastrado!")

# busca por autor
print("\n=== Busca por autor ===")
busca = input("Digite o autor: ").lower()
encontrado = False

for livro in catalogo:
    # compara ignorando maiusculo/minusculo
    if busca in livro["autor"].lower():
        print(livro["titulo"], "-", livro["autor"])
        encontrado = True

if not encontrado:
    print("Nenhum livro encontrado.")

# emprestimo ou devolucao
print("\n=== Emprestimo ou devolucao ===")
titulo_busca = input("Digite o titulo do livro: ").lower()
encontrado = False

for livro in catalogo:
    # procura pelo titulo
    if titulo_busca in livro["titulo"].lower():
        livro["disponivel"] = not livro["disponivel"]
        encontrado = True
        if livro["disponivel"]:
            print("Livro devolvido.")
        else:
            print("Livro emprestado.")

if not encontrado:
    print("Livro nao encontrado.")

# relatorio final
print("\n=== Relatorio Final ===")
total = len(catalogo)
disponiveis = 0
emprestados = 0

# conta livros disponiveis e emprestados
for livro in catalogo:
    if livro["disponivel"]:
        disponiveis += 1
    else:
        emprestados += 1

print("Total de livros:", total)
print("Disponiveis:", disponiveis)
print("Emprestados:", emprestados)

print("\nLivros emprestados:")
for livro in catalogo:
    if not livro["disponivel"]:
        print("-", livro["titulo"])