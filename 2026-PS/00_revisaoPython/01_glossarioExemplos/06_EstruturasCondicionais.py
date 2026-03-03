# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 06_EstruturasCondicionais.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Tomada de Decisão (if, elif, else).
    Baseado integralmente no "Glossário 07 - Estruturas Condicionais".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: O "cérebro" do programa e a analogia da encruzilhada.
    2. Sintaxe Básica: if, if/else e if/elif/else.
    3. Regra de Ouro: Indentação (4 espaços) e os dois pontos (:).
    4. Recursos Modernos: match/case (Python 3.10+) e Operador Ternário.
    5. Lógica Avançada: If aninhado, operadores lógicos e pertinência (in).
    6. Erros Comuns: Atribuição no if, ordem dos elifs.
    7. Exemplo Integrador: Calculadora de Frete.

==============================================================================
"""

import sys
import time

def limpar_tela():
    """Limpa visualmente o terminal."""
    print("\n" * 5)
    print("=" * 80)

def esperar():
    """Pausa para leitura."""
    input("\n[Pressione ENTER para continuar...]")

def mostrar_codigo_didatico(codigo):
    """Exibe o código com numeração e destaque para os comentários."""
    print("\n📄 CÓDIGO EM ANÁLISE (Observe a INDENTAÇÃO e os COMENTÁRIOS #):")
    print("-" * 80)
    linhas = codigo.strip().split('\n')
    for i, linha in enumerate(linhas):
        print(f"{i+1:02d} | {linha}")
    print("-" * 80)
    print("\n▶️  INICIANDO EXECUÇÃO PASSO A PASSO...\n")
    time.sleep(1.5)
    return linhas

def executar_linha(numero_linha, atraso=0.8):
    """Simula o processamento da linha."""
    print(f"⚙️  [Lendo Linha {numero_linha:02d}]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha {numero_linha:02d}]   ")

# ==============================================================================
# TÓPICO 1: SINTAXE BÁSICA E INDENTAÇÃO
# ==============================================================================
def sintaxe_basica():
    limpar_tela()
    print("🔹 TÓPICO 1: IF, ELSE E A IMPORTÂNCIA DA INDENTAÇÃO")
    print("-" * 80)
    print("Estruturas condicionais permitem que o programa tome decisões.")
    print("⚠️ REGRA DE OURO: Em Python, usamos 4 ESPAÇOS para definir o bloco.")
    print("   Não usamos chaves {} como em Java ou C. A indentação manda!")
    print("-" * 80)

    # Baseado nos Exemplos 1, 2 e 3 do Glossário
    codigo = """nota = float(input("Digite a nota (0-10): "))

# 1. Estrutura' if/elif/else (Note os 4 espaços e os dois pontos :)
if nota >= 9.0:
    print("Conceito A - Excelente")  # Só executa se nota >= 9
elif nota >= 7.0:
    print("Conceito B - Bom")        # Só executa se nota >= 7 E nota < 9
elif nota >= 5.0:
    print("Conceito C - Regular")    # Só executa se nota >= 5 E nota < 7
else:
    print("Conceito D/E - Reprovado") # Executa se NENHUMA anterior for True

print("Fim da análise.") # Executa sempre (está fora da indentação)"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    try:
        nota = float(input("   ↳ AÇÃO USUÁRIO (Digite uma nota, ex: 8.5): "))
    except ValueError:
        nota = 0.0
        print("   (Valor inválido, assumindo 0.0)")

    print(f"\n   ⚖️  [AVALIANDO CONDICIONAIS PARA NOTA {nota}]")
    
    executar_linha(4)
    print(f"   ↳ TESTE 1: {nota} >= 9.0? {'Sim' if nota >= 9 else 'Não'}")
    
    if nota >= 9.0:
        print("   ↳ CAMINHO: Entrou no primeiro IF.")
        executar_linha(5)
        print("   ↳ SAÍDA: Conceito A - Excelente")
        print("   ↳ PULO: Ignorando o restante da estrutura (elif/else)...")
    else:
        print("   ↳ CAMINHO: Pulou para o próximo ELIF.")
        executar_linha(6)
        print(f"   ↳ TESTE 2: {nota} >= 7.0? {'Sim' if nota >= 7 else 'Não'}")
        
        if nota >= 7.0:
            print("   ↳ CAMINHO: Entrou no primeiro ELIF.")
            executar_linha(7)
            print("   ↳ SAÍDA: Conceito B - Bom")
            print("   ↳ PULO: Ignorando o restante...")
        else:
            print("   ↳ CAMINHO: Pulou para o próximo ELIF.")
            executar_linha(8)
            print(f"   ↳ TESTE 3: {nota} >= 5.0? {'Sim' if nota >= 5 else 'Não'}")
            
            if nota >= 5.0:
                print("   ↳ CAMINHO: Entrou no segundo ELIF.")
                executar_linha(9)
                print("   ↳ SAÍDA: Conceito C - Regular")
            else:
                print("   ↳ CAMINHO: Nenhuma condição atendida. Caindo no ELSE.")
                executar_linha(10)
                executar_linha(11)
                print("   ↳ SAÍDA: Conceito D/E - Reprovado")

    executar_linha(13)
    print("   ↳ SAÍDA: Fim da análise.")
    
    esperar()

# ==============================================================================
# TÓPICO 2: MATCH / CASE (PYTHON 3.10+)
# ==============================================================================
def match_case_demo():
    limpar_tela()
    print("🔹 TÓPICO 2: MATCH / CASE (O 'SWITCH' DO PYTHON)")
    print("-" * 80)
    print("Disponível a partir do Python 3.10, é ideal para menus de opções.")
    print("Sintaxe mais limpa que vários if/elif/elif.")
    print("-" * 80)
    
    # Baseado na seção match/case do Glossário
    codigo = """opcao = input("Escolha (1-3): ")

match opcao:             # Analisa a variável 'opcao'
    case "1":            # Caso seja "1"
        print("Opção 1: Iniciar Jogo")
    case "2":            # Caso seja "2"
        print("Opção 2: Configurações")
    case "3":            # Caso seja "3"
        print("Opção 3: Sair")
    case _:              # _ funciona como 'default' ou 'else'
        print("Opção Inválida!")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    opcao = input("   ↳ AÇÃO USUÁRIO (Digite 1, 2, 3 ou outro): ")
    
    executar_linha(3)
    print(f"   ↳ MATCH: Analisando o valor '{opcao}'...")
    
    encontrou = False
    
    executar_linha(4)
    if opcao == "1":
        print("   ↳ MATCH: Casou com '1'.")
        executar_linha(5)
        print("   ↳ SAÍDA: Opção 1: Iniciar Jogo")
        encontrou = True
    
    if not encontrou:
        executar_linha(6)
        if opcao == "2":
            print("   ↳ MATCH: Casou com '2'.")
            executar_linha(7)
            print("   ↳ SAÍDA: Opção 2: Configurações")
            encontrou = True
            
    if not encontrou:
        executar_linha(8)
        if opcao == "3":
            print("   ↳ MATCH: Casou com '3'.")
            executar_linha(9)
            print("   ↳ SAÍDA: Opção 3: Sair")
            encontrou = True
            
    if not encontrou:
        executar_linha(10)
        print("   ↳ MATCH: Caiu no caso coringa (_).")
        executar_linha(11)
        print("   ↳ SAÍDA: Opção Inválida!")
        
    esperar()

# ==============================================================================
# TÓPICO 3: OPERADOR TERNÁRIO
# ==============================================================================
def operador_ternario():
    limpar_tela()
    print("🔹 TÓPICO 3: OPERADOR TERNÁRIO (IF EM UMA LINHA)")
    print("-" * 80)
    print("Sintaxe: valor_se_verdadeiro IF condicao ELSE valor_se_falso")
    print("Útil para atribuições simples e f-strings.")
    print("-" * 80)
    
    # Baseado no Exemplo 6 e Seção Ternário do Glossário
    codigo = """idade = int(input("Idade: "))

# Forma Clássica (4 linhas)
# if idade >= 18: status = "Maior"
# else: status = "Menor"

# Forma Ternária (1 linha)
status = "Maior" if idade >= 18 else "Menor"
print(f"Status: {status}")

# Ternário dentro do print (F-string)
n = 10
print(f"O número {n} é {'Par' if n % 2 == 0 else 'Ímpar'}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    try:
        idade = int(input("   ↳ AÇÃO USUÁRIO (Digite idade): "))
    except: idade = 18

    executar_linha(8)
    print(f"   ↳ AVALIAÇÃO: {idade} >= 18? {'Sim' if idade >= 18 else 'Não'}")
    status = "Maior" if idade >= 18 else "Menor"
    print(f"   ↳ ATRIBUIÇÃO: Variável 'status' recebeu '{status}'")
    
    executar_linha(9)
    print(f"   ↳ SAÍDA: Status: {status}")
    
    executar_linha(12)
    n = 10
    
    executar_linha(13)
    print("   ↳ AVALIAÇÃO INTERNA: 10 % 2 == 0? Sim -> 'Par'")
    print(f"   ↳ SAÍDA: O número 10 é Par")
    
    esperar()

# ==============================================================================
# TÓPICO 4: LÓGICA COMPLEXA (ANINHADA E OPERADORES)
# ==============================================================================
def logica_complexa():
    limpar_tela()
    print("🔹 TÓPICO 4: IF ANINHADO E OPERADORES LÓGICOS")
    print("-" * 80)
    print("Podemos colocar um IF dentro de outro (Aninhamento).")
    print("Também usamos AND, OR, NOT e IN para combinar condições.")
    print("-" * 80)
    
    # Baseado nos Exemplos 4, 5 e 8 do Glossário
    codigo = """# 1. Pertinência com 'in' (Mais elegante que vários OR)
dia = "sábado"
if dia in ["sábado", "domingo"]:
    print("🎉 Fim de semana!")

# 2. If Aninhado (Um if dentro do outro)
sexo = "M"
peso = 90
if sexo == "M":
    if peso >= 80:    # Indentação dupla (8 espaços)
        print("Masculino Pesado")
    else:
        print("Masculino Leve")

# 3. Operadores Lógicos (and/not)
habilitado = False
maior_idade = True
if maior_idade and not habilitado:
    print("⚠️ Pode tirar carteira, mas não pode dirigir ainda.")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2); executar_linha(3)
    print("   ↳ LÓGICA: 'sábado' está na lista? Sim.")
    executar_linha(4)
    print("   ↳ SAÍDA: 🎉 Fim de semana!")
    
    executar_linha(7); executar_linha(8)
    
    executar_linha(9)
    print("   ↳ TESTE 1: Sexo é M? Sim. Entrando no bloco...")
    
    executar_linha(10)
    print("   ↳ TESTE 2 (Aninhado): Peso >= 80? Sim.")
    
    executar_linha(11)
    print("   ↳ SAÍDA: Masculino Pesado")
    
    executar_linha(16); executar_linha(17)
    
    executar_linha(18)
    print("   ↳ LÓGICA: (True) AND (NOT False) -> True AND True -> True")
    
    executar_linha(19)
    print("   ↳ SAÍDA: ⚠️ Pode tirar carteira, mas não pode dirigir ainda.")
    
    esperar()

# ==============================================================================
# TÓPICO 5: ERROS COMUNS
# ==============================================================================
def erros_comuns():
    limpar_tela()
    print("🔹 TÓPICO 5: ERROS COMUNS")
    print("-" * 80)
    print("1. Esquecer os dois pontos (:).")
    print("2. Errar a indentação (misturar tab com espaço ou alinhar errado).")
    print("3. Usar '=' (atribuição) em vez de '==' (comparação).")
    print("4. Ordem errada dos ELIFs (sempre do mais específico para o geral).")
    print("-" * 80)
    
    # Baseado na seção Erros Comuns do Glossário
    codigo = """nota = 8

# ❌ ERRO DE LÓGICA (Ordem errada):
if nota >= 5:          # Esta condição é muito ampla e "rouba" as outras!
    print("Passou")    # O 8 entra aqui e o programa para.
elif nota >= 7:
    print("Bom")       # Nunca será executado para 8!
elif nota >= 9:
    print("Excelente") # Nunca será executado!

# ✅ CORREÇÃO (Do mais restritivo para o mais amplo):
# if nota >= 9: ...
# elif nota >= 7: ...
# elif nota >= 5: ..."""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ MEMÓRIA: nota = 8")
    
    executar_linha(4)
    print("   ↳ TESTE: 8 >= 5? Sim! Entra aqui.")
    
    executar_linha(5)
    print("   ↳ SAÍDA: Passou")
    print("   ⚠️  PROBLEMA: O aluno tirou 8 (Bom), mas o sistema disse apenas 'Passou'.")
    print("       Como a primeira condição foi verdadeira, o Python ignorou o resto.")
    
    esperar()

# ==============================================================================
# TÓPICO 6: DESAFIO INTEGRADOR (FRETE)
# ==============================================================================
def desafio_frete():
    limpar_tela()
    print("🔹 DESAFIO FINAL: CALCULADORA DE FRETE")
    print("Integra: if/elif/else, in, and, strip/title e formatação.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """valor = float(input("Valor Compra: "))
regiao = input("Região: ").strip().title()

if valor >= 200:
    frete = 0
    msg = "FRETE GRÁTIS!"
elif regiao in ["Sul", "Sudeste"]:
    frete = 15.0
elif regiao == "Centro-Oeste":
    frete = 25.0
elif regiao in ["Norte", "Nordeste"]:
    frete = 35.0
else:
    frete = 0
    msg = "Região Inválida"

total = valor + frete"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Coletando Dados]...")
        valor = float(input("   Valor da compra (R$): "))
        regiao = input("   Região (Sul/Sudeste/Nordeste/Norte/Centro-Oeste): ").strip().title()
        
        print(f"\n⚙️  [Analisando Regras para {regiao} - R$ {valor:.2f}]...")
        time.sleep(1)
        
        msg = ""
        frete = 0.0
        
        # Simulação da lógica
        if valor >= 200:
            print("   ✅ Condição (valor >= 200) Verdadeira -> Frete Grátis aplicado.")
            frete = 0.0
            msg = "🎉 FRETE GRÁTIS!"
        elif regiao in ["Sul", "Sudeste"]:
            print(f"   ✅ Região '{regiao}' encontrada no grupo 1 (Sul/Sudeste).")
            frete = 15.0
            msg = "📦 Frete Padrão"
        elif regiao == "Centro-Oeste":
            print(f"   ✅ Região '{regiao}' encontrada no grupo 2.")
            frete = 25.0
            msg = "📦 Frete Intermediário"
        elif regiao in ["Norte", "Nordeste"]:
            print(f"   ✅ Região '{regiao}' encontrada no grupo 3 (Norte/Nordeste).")
            frete = 35.0
            msg = "📦 Frete Estendido"
        else:
            print("   ❌ Nenhuma regra atendida (Região desconhecida).")
            msg = "❌ Região Inválida (Frete zerado para evitar erro de cálculo)"
            
        total = valor + frete
        
        print("\n" + "="*40)
        print(f"🛒 Compra:  R$ {valor:.2f}")
        print(f"🚚 Frete:   R$ {frete:.2f} ({msg})")
        print("-" * 40)
        print(f"💰 TOTAL:   R$ {total:.2f}")
        print("="*40)
            
    except ValueError:
        print("\n❌ ERRO: O valor da compra deve ser numérico.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE CONDICIONAIS (GLOSSÁRIO 07)".center(80))
        print("=" * 80)
        print("1. Sintaxe Básica (if/elif/else) e Indentação")
        print("2. Recurso Moderno: match/case (Switch do Python)")
        print("3. Operador Ternário (If em uma linha)")
        print("4. Lógica Complexa (Aninhamento e Operadores)")
        print("5. Erros Comuns (Ordem e Atribuição)")
        print("6. Desafio Integrador: Calculadora de Frete")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': sintaxe_basica()
        elif opcao == '2': match_case_demo()
        elif opcao == '3': operador_ternario()
        elif opcao == '4': logica_complexa()
        elif opcao == '5': erros_comuns()
        elif opcao == '6': desafio_frete()
        elif opcao == '0':
            print("\nEncerrando laboratório... Escolha o caminho certo! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()