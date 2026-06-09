# Importamos la librería permitida para expresiones regulares
import re

# Texto dado en el enunciado
texto = """
Juan: 987654321
María: 912345678
Pedro: 998877665
Ana: 923456789
"""

# a) Extraer todos los números telefónicos
# Usamos findall y el patrón '[0-9]+' para extraer las secuencias de dígitos
numeros = re.findall('[0-9]+', texto)

print("a) Números telefónicos extraídos:" , numeros)
print("------------------------------------------------------------------------")


# b) Mostrar la cantidad total de números encontrados
# Usamos la función len() para contar cuántos elementos hay en la lista generada
cantidad_total = len(numeros)

print("\nb) Cantidad total de números encontrados:" , cantidad_total)
print("------------------------------------------------------------------------")