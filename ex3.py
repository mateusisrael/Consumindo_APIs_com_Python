''' 
Mateus Israel, 7 de novembro de 2018
Consumindo APIs com python
Exemplo 3:
'''
import requests
import json

cep = str(input('Cep: '))
url = 'https://viacep.com.br/ws/' + cep + '/json/'
print('GET para: ' + url)
http_req = requests.get(url)

print('')

print('JSON: \n' + http_req.text)

print('')

dicionario = json.loads(http_req.text)
print('Dicionário:\n' , dicionario)