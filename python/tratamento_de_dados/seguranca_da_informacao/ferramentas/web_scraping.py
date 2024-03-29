"""Implementa um web scraping"""
from bs4 import BeautifulSoup
import requests

# Objeto site recebendo o conteúdo da requisição http do site...
site = requests.get('http://www.climatempo.com.br', timeout=10).content
# Objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')
# Transforma html em string e o print vai exibir o html
# print(soup.prettify())
print(soup.a.string)
