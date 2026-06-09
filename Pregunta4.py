from Pregunta3 import precios, titulos
import pandas as pd

df_libros = pd.DataFrame({"Título": titulos, "Precio": precios})

print(df_libros)