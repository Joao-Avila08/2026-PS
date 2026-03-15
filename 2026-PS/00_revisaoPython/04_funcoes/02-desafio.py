#======================================================
# SISTEMA DE BIBLIOTECA
#======================================================
# Disciplina : Programação de Sistemas (PS)
# Autor      : João Vitor Gracietti De Ávila
# Data       : 09/03/2026
# Repositório: https://github.com/Joao-Avila08/2026-PS
#======================================================
# DESCRICAO:
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_situacao(media):
    if media >= 6.0:
        return "Aprovado"
    elif 4.0 <= media < 6.0:
        return "Recuperação"
    else:
        return "Reprovado"

def solicitar_notas(nome_aluno):
    while True:
        try:
            nota1 = float(input(f"Informe a primeira nota de {nome_aluno}: "))
            nota2 = float(input(f"Informe a segunda nota de {nome_aluno}: "))
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                return nota1, nota2
            else:
                print("Notas devem estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def gerar_relatorio(nome, media, situacao):
    print("\n" + "-" * 30)
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)

def main():
    lista_alunos = []

    for i in range(1, 4):
        nome = input(f"Digite o nome do {i}º aluno: ")
        nota1, nota2 = solicitar_notas(nome)
        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)
        gerar_relatorio(nome, media, situacao)

        lista_alunos.append({
            'nome': nome,
            'media': media,
            'situacao': situacao
        })

if __name__ == "__main__":
    main()