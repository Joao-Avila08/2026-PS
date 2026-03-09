# ==================================================
# SISTEMA DE CONVERSÃO DE UNIDADES
# ==================================================

# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 – Revisão: Módulos
# Autor      : Joao Vitor Gracietti De Ávila
# Data       : 05/03/26
# Repositório: https://github.com/Joao-Avila08/2026-PS.git
# ==================================================

# ---- BLOCO 1: STDLIB ----

import math                         # importa o módulo inteiro
from random import randint, choice  # importa apenas funções específicas
from datetime import datetime       # importa a classe datetime do módulo datetime

print("=== Explorando a Stdlib ===")

print(f"π = {math.pi:.4f}")
print(f"√2 = {math.sqrt(2):.4f}")

print(f"Número aleatório: {randint(1, 100)}")

print(f"Unidade sorteada: {choice(['km', 'milhas', 'metros'])}")

print(f"Agora: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
# ---- BLOCO 2: MÓDULO PRÓPRIO ----

from conversores import temperatura     # importa o módulo do pacote

print("\n=== Conversão de Temperatura ===")

valor = 100.0

print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f}°F")
print(f"{valor}°C = {temperatura.celsius_para_kelvin(valor):.2f} K")
print(f"Zero absoluto: {temperatura.ZERO_ABSOLUTO_CELSIUS}°C")
# ---- BLOCO 3: API LIMPA DO PACOTE ----
from conversores import km_para_milhas, celsius_para_fahrenheit
# Funciona porque __init__.py ja expos essas funções

print("\n=== API Limpa ===")
print(f"100 km = {km_para_milhas (100):.2f}milhas")
print(f"25°C  = {celsius_para_fahrenheit(25):.lf}°F")

#----BLOCO 4: CAMADAS----
from utils import cabecalho_secao, formatar_resultado
print(cabecalho_secao("Conversões de Distância"))
print(formatar_resultado("km->mi"100,"km",km_para_milhas(100),"mi"))