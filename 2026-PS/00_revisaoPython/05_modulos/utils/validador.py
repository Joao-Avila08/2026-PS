def validar_numero(valor_str, minimo=None, maximo=None):
    try:
        numero = float(valor_str)

        if minimo is not None and numero < minimo:
            return False, f"Valor deve ser >= {minimo}"

        if maximo is not None and numero > maximo:
            return False, f"Valor deve ser <= {maximo}"

        return True, numero

    except ValueError:
        return False, "Entrada inválida. Digite um número."