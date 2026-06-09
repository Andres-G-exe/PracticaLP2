import re

# 1. Definimos el texto original
texto = """
correo1@gmail.com
ventas@empresa.pe
contacto@universidad.edu.pe
soporte@hotmail.com
"""

# 2. Patrón
patron_correo = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# a) Extraemos las direcciones de correo electrónico
correos_encontrados = re.findall(patron_correo, texto)

# 3. Mostramos los resultados
print("=== RESULTADOS DEL ANÁLISIS ===")
print(f"a) Correos extraídos:")
for correo in correos_encontrados:
    print(f"{correo}")

print(f"b) Total de correos encontrados: {len(correos_encontrados)}")