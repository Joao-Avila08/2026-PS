# conversores/__init__.py
# Expoe a API pública do pacote.

from .temperatura import celsius_para_fahrenheit, celsius_para_kevin,fahrenheit_para_celsius
from .distancia import km_para_milhas, milhas_para_km, metros_para_pes

# O ". antes do nome" = importação relativa imodulo dentro deste pacote)
__all__={
    "celsius_para_fahrenheit","celsius_para_kelvin","fahrenheit_para_celsius","km_para_milhas", "milhas_para_km","metros_para_pes",
    
}