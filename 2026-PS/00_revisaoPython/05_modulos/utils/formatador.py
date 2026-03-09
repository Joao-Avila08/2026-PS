# utils/formatador.py

def linha_separadora(char="=", largura=40):
    """retrona uma linha separadora"""
    return char * largura
def formatar_resultado(origem, valor_original, unidade_origem, valor_convertido, unidade_destino):
    """formata a exibição de um resultado de conversao."""
    return f" {origem}: {valor_original:.2f} {unidade_origem} -> {valor_convertido:.4f} {unidade_destino} "
def cabecalho_secao(titulo):
    """retorna um cabecalho de seção formatado."""
    sep = linha_separadora("-", len(titulo)+ 4)
    return f"\n{sep}\n {titulo}\n{sep}"