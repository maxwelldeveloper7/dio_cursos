"""Implementa um verificador de ip externo"""
import json
from urllib.request import urlopen

URL = 'https://ipinfo.io/json'

resposta = urlopen(URL)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print(f'IP: {ip}\nRegião: {regiao}\nPais: {pais}\nCidade: {cidade}\nOrg: {org}')
