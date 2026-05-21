
#Diciplina: Programação de Sistemas               #                               #
#data: 28/03/2025                                 #
#autor: Joao Avila                                #
#=================================================#
import pickle
class Pet:
    def __init__(self,nome,especie,idade,peso,vacinado,dono):
        self.nome=nome
        self.especie=especie
        self.idade=idade
        self.peso=peso
        self.vacinado=vacinado
        self.dono=dono
        self.hospedado=False

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Vacinado: {self.vacinado}")
        print(f"Dono: {self.dono}")
        print(f"Hospedado: {self.hospedado}")

    def registrar_entrada(self):
        self.hospedado=True
        print("Check-in realizado")

    def registrar_saida(self):
        self.hospedado=False
        print("Check-out realizado")

    def calcular_diaria(self):
        return 50
    
    def verificar_vacinacao(self):
        if self.vacinado.lower()=="sim":
            print("Vacinação em dia")
        else:
            print("Vacinação pendente")

    def atualizar_peso(self,novo_peso):
        self.peso=novo_peso
        print("Peso atualizado")

    def emitir_resumo(self):
        self.exibir_dados()
        print(f"Diária: R$ {self.calcular_diaria()}")

    def para_linha_txt(self):
        return f"{self.nome};{self.especie};{self.idade};{self.peso};{self.vacinado};{self.dono};{self.hospedado}"
    
def salvar_em_txt(pets,caminho):
    with open(caminho,"w",encoding="utf-8") as arquivo:
        for p in pets:
            arquivo.write(p.para_linha_txt()+"\n")
    print(f"{len(pets)} pet(s) salvo(s)")

def carregar_de_txt(caminho):
    pets=[]
    try:
        with open(caminho,"r",encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha=linha.strip()
                if not linha:
                    continue
                partes=linha.split(";")
                nome,especie,idade,peso,vacinado,dono,hospedado=partes
                pet=Pet(nome,especie,int(idade),float(peso),vacinado,dono)
                pet.hospedado=hospedado=="True"
                pets.append(pet)
    except FileNotFoundError:
        print("Arquivo ainda não existe")
    return pets

def salvar_em_binario(pets,caminho):
    with open(caminho,"wb") as arquivo:
        pickle.dump(pets,arquivo)
    print(f"{len(pets)} pet(s) salvo(s)")

def carregar_de_binario(caminho):
    try:
        with open(caminho,"rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print("Arquivo ainda não existe")
        return []
    
def cadastrar(pets):
    nome=input("Nome: ")
    especie=input("Espécie: ")
    idade=int(input("Idade: "))
    peso=float(input("Peso: "))
    vacinado=input("Vacinado: ")
    dono=input("Dono: ")
    pets.append(Pet(nome,especie,idade,peso,vacinado,dono))
    print("Pet cadastrado")

def listar(pets):
    if not pets:
        print("Nenhum pet cadastrado")
        return
    for i,p in enumerate(pets,start=1):
        print(f"\n[{i}]")
        p.exibir_dados()

def selecionar_pet(pets):
    listar(pets)
    if not pets:
        return None
    indice=int(input("Número do pet: "))-1
    if 0<=indice<len(pets):
        return pets[indice]
    else:
        print("Índice inválido")
        return None
    
def checkin(pets):
    pet=selecionar_pet(pets)
    if pet:
        pet.registrar_entrada()

def checkout(pets):
    pet=selecionar_pet(pets)
    if pet:
        pet.registrar_saida()

def atualizar_peso_pet(pets):
    pet=selecionar_pet(pets)
    if pet:
        novo_peso=float(input("Novo peso: "))
        pet.atualizar_peso(novo_peso)

def buscar_pet(pets):
    busca=input("Buscar nome: ").lower()
    for p in pets:
        if busca in p.nome.lower():
            p.exibir_dados()

def relatorio_hospedados(pets):
    total=0
    for p in pets:
        if p.hospedado:
            p.exibir_dados()
            total+=p.calcular_diaria()
    print(f"Total do dia: R$ {total}")

def resumo_pet(pets):
    pet=selecionar_pet(pets)
    if pet:
        pet.emitir_resumo()

def menu():
    pets=carregar_de_binario("2026-PS/02_poo/hotel_pets_v2/pets.bin")
    while True:
        print("\n1-Cadastrar pet")
        print("2-Listar pets")
        print("3-Check-in")
        print("4-Check-out")
        print("5-Atualizar peso")
        print("6-Buscar pet")
        print("7-Relatório hospedados")
        print("8-Resumo individual")
        print("9-Salvar txt")
        print("10-Salvar binário")
        print("0-Sair")
        opcao=input("Opção: ")

        if opcao=="1":
            cadastrar(pets)
        elif opcao=="2":
            listar(pets)
        elif opcao=="3":
            checkin(pets)
        elif opcao=="4":
            checkout(pets)
        elif opcao=="5":
            atualizar_peso_pet(pets)
        elif opcao=="6":
            buscar_pet(pets)
        elif opcao=="7":
            relatorio_hospedados(pets)
        elif opcao=="8":
            resumo_pet(pets)
        elif opcao=="9":
            salvar_em_txt(pets,"2026-PS/02_poo/hotel_pets_v2/pets.txt")
        elif opcao=="10":
            salvar_em_binario(pets,"2026-PS/02_poo/hotel_pets_v2/pets.bin")
        elif opcao=="0":
            salvar_em_txt(pets,"2026-PS/02_poo/hotel_pets_v2/pets.txt")
            salvar_em_binario(pets,"2026-PS/02_poo/hotel_pets_v2/pets.bin")
            print("Até logo!")
            break
        else:
            print("Opção inválida")
if __name__=="__main__":
    menu()