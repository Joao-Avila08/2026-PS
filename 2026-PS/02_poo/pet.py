'''
=====================================================
#arquivo: pet.py
#disciplica: programação de sistemas (2026-2)
#aula: aula 20 - por que poo?
#autor: Joao Vitor G. De Ávila
#conceitos: classe, objeto, atributos, metodos, encapsulamento
#atividade: classe pet
======================================================
'''
class Pet:
    def __init__(self, nome, especie, idade, nome_dono, raca, peso, vacinado):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.nome_dono = nome_dono
        self.raca = raca
        self.peso = peso
        self.vacinado = vacinado
        self.hospedado = False

    def exibir_dados(self):
        print("\n---Dados do Pet---")
        print(f"Nome:{self.nome}")
        print(f"Especie:{self.especie}")
        print(f"Idade:{self.idade}")
        print(f"Nome do dono:{self.nome_dono}")
        print(f"Hospedado:{'Sim' if self.hospedado else 'Não'}")
        print(f"raça:{self.raca}")
        print(f"peso:{self.peso}")
        print(f"vacinado:{'Sim' if self.vacinado else 'Não'}")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"{self.nome} ja esta hospedado")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"{self.nome} nao esta hospedado")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel")

    def calcular_diaria(self):
        if self.idade < 3:
            return 50.00
        elif self.idade < 10:
            return 60.00
        else:
            return 75.00

    def verificar_vacinacao(self):
        if self.vacinado:
            print(f"{self.nome} vacinacao em dia")
        else:
            print(f"{self.nome} atenção: vacinacao pendente")

    def atualizar_peso(self, atualizar_peso):
        self.peso = atualizar_peso
        print(f"{self.nome} peso atualizado para {self.peso} kg")

    def emitir_resumo(self):
        print("\n---Resumo do Pet---")
        print(f"Nome:{self.nome}")
        print(f"Especie:{self.especie}")
        print(f"Idade:{self.idade}")
        print(f"Nome do dono:{self.nome_dono}")
        print(f"valor diaria:{self.calcular_diaria():.2f}")
        print(f"hospedado:{'Sim' if self.hospedado else 'Não'}")
        print(f"Peso:{self.peso} kg")
        print(f"Vacinado:{'Sim' if self.vacinado else 'Não'}")


pet1 = Pet("Rex", "Cachorro", 5, "Maria", "Labrador", 22.5, True)
pet2 = Pet("Mimi", "Gato", 2, "João", "Siamês", 4.2, True)
pet3 = Pet("Thor", "Cachorro", 11, "Ana", "Vira-lata", 18.0, False)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.verificar_vacinacao()
print("Diária:", pet1.calcular_diaria())
pet1.atualizar_peso(23.0)
pet1.emitir_resumo()

pet3.exibir_dados()
pet3.verificar_vacinacao()
pet3.registrar_entrada()
pet3.registrar_saida()