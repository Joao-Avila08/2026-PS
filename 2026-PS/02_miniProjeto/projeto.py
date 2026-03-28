#=================================================#
#       SISTEMA DO INTERCLASSES IFPR              #
#=================================================#
#Diciplina: Programação de Sistemas               #
#Aula: numero 13                                  #
#data: 28/03/2025                                 #
#autores: Bruno de Paula, João Ávila, João Mauda  #
#=================================================#
#                    OBJETIVO                     #
# Realizar um sistemas que ajude na organização do#
# Interclasses, que:                              #
# Liste os times                                  #
# Adicione os times                               #
# Busque time                                     # 
# Elimine os times                                #
# Reative os times eliminados                     #
#=================================================#
# --- CONFIGURAÇÕES ---
ARQUIVO = "2026-PS/02_miniProjeto/dados.txt"  # Onde as informações ficam guardadas 
SEPARADOR = "|"        # O símbolo que usamos para separar os dados no arquivo

from datetime import datetime  # Para registrar data e hora no histórico
ARQUIVO_HISTORICO = "2026-PS/02_miniProjeto/historico.txt"  # Arquivo de histórico

#=================================================#
#               FUNÇÕES DO SISTEMA               #
#=================================================#

def listar_times(F):
    """Mostra na tela todos os times que estão na memória."""
    print("\n" + "=" * 50)
    print("   TIMES DO INTERCLASSE")
    print("=" * 50)

    # Se a lista estiver vazia, avisa o usuário e para por aqui
    if not F:
        print("  Nenhum time cadastrado.")
        return

    # O enumerate cria o numerozinho (i) para o usuário escolher depois
    for i, time in enumerate(F, 1):
        status = "✅ Inscrito" if time["inscrito"] else "❌ Eliminado"
        print(f"  {i}. {time['turma']} - Líder: {time['lider']} [{status}]")

    print("=" * 50)


def adicionar_time(F):
    """Cria um novo time e já salva no arquivo para não perder."""
    print("\n--- Adicionar Novo Time ---")

    turma = input("Turma: ").strip()
    lider = input("Líder: ").strip()

    # Validação simples para não aceitar nomes vazios
    if not turma or not lider:
        print("⚠️ Turma e líder são obrigatórios.")
        return

    # Validação para não cadastrar duplicados
    if any(t["turma"].lower() == turma.lower() for t in F):
        print("⚠️ Esta turma já está cadastrada.")
        return

    # Adiciona as informações em formato de dicionário na nossa lista
    F.append({
        "turma": turma,
        "lider": lider,
        "inscrito": True  # Todo time começa inscrito por padrão
    })

    salvar_dados(F)  # Atualiza o arquivo txt
    registrar_historico("ADICIONADO", {"turma": turma, "lider": lider})  # Registra no histórico
    print(f"✅ Time '{turma}' cadastrado com sucesso!")


def buscar_time(F):
    """Procura times pelo nome da turma (mesmo que seja só um pedaço do nome)."""
    print("\n--- Buscar Time ---")
    termo = input("Digite parte da turma: ").strip().lower()

    # Cria uma sub-lista apenas com os times que batem com a busca
    resultados = [t for t in F if termo in t["turma"].lower()]

    if not resultados:
        print("Nenhum time encontrado.")
        return

    for time in resultados:
        status = "Inscrito" if time["inscrito"] else "Eliminado"
        print(f" • {time['turma']} - Líder: {time['lider']} [{status}]")


def eliminar_time(F):
    """Muda o status de um time para 'Eliminado'."""
    listar_times(F)

    if not F:
        return

    print("\n--- Eliminar Time ---")
    try:
        # Pega o número que o usuário vê na tela e subtrai 1 para achar a posição na lista
        numero = int(input("Número do time: "))
        time = F[numero - 1]

        if not time["inscrito"]:
            print("⚠️ Time já está eliminado.")
        else:
            time["inscrito"] = False  # Muda o status
            salvar_dados(F)           # Salva a alteração no arquivo
            registrar_historico("ELIMINADO", time)  # Registra no histórico
            print(f"❌ Time '{time['turma']}' eliminado.")
    except:
        print("❌ Entrada inválida.")


def reativar_time(F):
    """Traz um time eliminado de volta para o jogo."""
    listar_times(F)

    if not F:
        return

    print("\n--- Reativar Time ---")
    try:
        numero = int(input("Número do time: "))
        time = F[numero - 1]

        if time["inscrito"]:
            print("⚠️ Time já está ativo.")
        else:
            time["inscrito"] = True
            salvar_dados(F)
            registrar_historico("REATIVADO", time)  # Registra no histórico
            print(f"✅ Time '{time['turma']}' reativado.")
    except:
        print("❌ Entrada inválida.")


def carregar_dados():
    """Lê o arquivo texto e transforma de volta em uma lista para o Python entender."""
    dados = []
    try:
        # Abre o arquivo apenas para leitura ("r")
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue

                # Divide a linha onde houver o separador "|"
                turma, lider, inscrito = linha.split(SEPARADOR)

                dados.append({
                    "turma": turma,
                    "lider": lider,
                    "inscrito": inscrito == "True"  # Converte o texto para valor lógico
                })
    except FileNotFoundError:
        # Se o arquivo não existir (primeira vez), não faz nada e retorna lista vazia
        pass

    return dados


def salvar_dados(F):
    """Pega a lista da memória e escreve tudo de novo no arquivo texto."""
    # O modo "w" limpa o arquivo e escreve tudo do zero (atualização total)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for time in F:
            linha = f"{time['turma']}{SEPARADOR}{time['lider']}{SEPARADOR}{time['inscrito']}\n"
            f.write(linha)


def registrar_historico(acao, time):
    """Registra a ação feita em um time com data e hora."""
    try:
        with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{data_hora} - {acao}: {time['turma']} - Líder: {time['lider']}\n")
    except Exception as e:
        print(f"❌ Erro ao registrar histórico: {e}")


def menu():
    """O centro de comando do programa."""
    dados = carregar_dados()  # Carrega os dados assim que o programa abre

    while True:
        print("\n🏆 SISTEMA DE INTERCLASSE")
        print("1. Listar times")
        print("2. Adicionar time")
        print("3. Buscar time")
        print("4. Eliminar time")
        print("5. Reativar time")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            listar_times(dados)
        elif op == "2":
            adicionar_time(dados)
        elif op == "3":
            buscar_time(dados)
        elif op == "4":
            eliminar_time(dados)
        elif op == "5":
            reativar_time(dados)
        elif op == "0":
            print("Até logo! 🖐️")
            break
        else:
            print("⚠️ Opção inválida.")


# Este bloco garante que o menu só inicie se você rodar este script diretamente
if __name__ == "__main__":
    menu()