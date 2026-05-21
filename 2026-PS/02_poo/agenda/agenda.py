"""
agenda.py - aula 23 (programação de sistemas - 2026)
Agenda de contatos com menu interativo e persistencia(.txt e binario).

"""
import pickle

class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print(f"  Nome  : {self.nome}")
        print(f"  Telefone : {self.telefone}")
        print(f"  Email  : {self.email}")

    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"


def salvar_em_txt(contatos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            arquivo.write(c.para_linha_txt() + "\n")
    print(f"/ ✅{len(contatos)} contato(s) salvo(s) em {caminho}")


def carregar_de_txt(caminho):
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return contatos


def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"/ ✅{len(contatos)} contato(s) salvo(s) em {caminho}")


def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
        return []
def cadastrar(contatos):
    print("\n--- Novo contato ---")
    nome = input("Nome : ")
    telefone = input("Telefone: ")
    email = input("Email : ")
    contatos.append(Contato(nome, telefone, email))
    print("✅ Contato cadastrado.")


def listar(contatos):
    if not contatos:
        print("\n(Agenda vazia!)")
        return

    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()


def remover(contatos):
    listar(contatos)

    if not contatos:
        return

    indice = int(input("\nNº do contato a remover: ")) - 1

    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"✅ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")


def menu():
    contatos = carregar_de_binario("2026-PS/agenda/agenda.bin")

    while True:
        print("\n========== AGENDA ==========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(contatos)

        elif opcao == "2":
            listar(contatos)

        elif opcao == "3":
            remover(contatos)

        elif opcao == "4":
            salvar_em_txt(contatos, "2026-PS/agenda/agenda.txt")

        elif opcao == "5":
            salvar_em_binario(contatos, "2026-PS/agenda/agenda.bin")

        elif opcao == "0":
            salvar_em_binario(contatos, "2026-PS/agenda/agenda.bin")
            print("Até logo!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()