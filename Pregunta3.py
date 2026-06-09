import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://books.toscrape.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")


titulos = [tag["title"] for tag in soup.select("article.product_pod h3 a")]
precios = [tag.get_text().strip() for tag in soup.select("article.product_pod .price_color")]


df_libros = pd.DataFrame({"Título": titulos, "Precio": precios})


print(df_libros)