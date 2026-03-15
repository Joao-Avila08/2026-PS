def kg_para_libras(kg):
    """Converte quilogramas para libras."""
    return kg * 2.20462

def kg_para_gramas(kg):
    """Converte quilogramas para gramas."""
    return kg * 1000


if __name__ == "__main__":
    print("Testes do módulo massa")
    print("10 kg em libras:", kg_para_libras(10))
    print("10 kg em gramas:", kg_para_gramas(10))