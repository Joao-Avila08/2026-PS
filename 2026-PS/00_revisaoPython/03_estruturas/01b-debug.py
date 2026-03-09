# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo",           "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente",         "autor": "Luciano Ramalho", "disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"]) #a lista começa em 0

print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True: # é true em vez de false, pois tem o livro disponivel
        print(f' ✅ {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():# sem o .items ele percorre apenas a chave esquece do valor
    print(f" {chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]#a chave foi declarada com autor e nao Autor
print("\nAutor do primeiro livro:", primeiro_autor)