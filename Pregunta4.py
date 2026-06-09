from Pregunta3 import precios, titulos
import pandas as pd

df_libros = pd.DataFrame({"Título": titulos, "Precio": precios})

print(df_libros)

df_libros.to_csv("libros.csv", index=False, encoding="utf-8")

# c) Determinar el más caro y más barato
libro_mas_caro = df_libros.loc[df_libros['Precio'].idxmax()]
libro_mas_barato = df_libros.loc[df_libros['Precio'].idxmin()]

# Mostrar resultados en pantalla
print(df_libros)
print("-" * 30)
print(f"Libro más caro: {libro_mas_caro['Título']} | Precio: £{libro_mas_caro['Precio']}")
print(f"Libro más barato: {libro_mas_barato['Título']} | Precio: £{libro_mas_barato['Precio']}")

df_libros.to_csv("libros.csv", index=False, encoding="utf-8")