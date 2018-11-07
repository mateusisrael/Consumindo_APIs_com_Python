''' 
Mateus Israel, 7 de novembro de 2018
Consumindo APIs com python
Exemplo 4:
'''
import requests
import json

cep = str(input('Cep: '))
url = 'https://viacep.com.br/ws/' + cep + '/json/'
print('GET para: ' + url)
http_req = requests.get(url)
dicionario = json.loads(http_req.text)

print('\n', 'Informações: \n',
    dicionario["cep"], '\n',
    dicionario["logradouro"], '\n',
    dicionario["bairro"], '\n',
    dicionario["localidade"], '\n')