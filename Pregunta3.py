# Importar libreris permitidas
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://books.toscrape.com/"

# Se extrae el html en formato texto
html = requests.get(url).text

# Se identifica todos los elementos del html
soup = BeautifulSoup(html, "html.parser")

# Obtenemos las etiquetas hmtl inspeccionando la pagina

# Se extrae los titulos en base a su etiqueta
titulos = [tag["title"] for tag in soup.select("article.product_pod h3 a")]

# Se extrae los precios en base a su etiqueta
precios = [tag.get_text().strip() for tag in soup.select("article.product_pod .price_color")]

# Se muestra lo obtenido
print("Primeros 20 libros listados")

for i in range(len(titulos)):
    print(f"{i + 1}. {titulos[i]}, precio: {precios[i]}")