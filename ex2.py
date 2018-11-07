''' 
Mateus Israel, 7 de novembro de 2018
Consumindo APIs com python
Exemplo 2:
'''

import requests

print("=" * 50)
print('\n\n')

####################################################

cep = str(input('Cep: '))
url = 'https://viacep.com.br/ws/' + cep + '/json/'
print('GET para: ' + url, '\n')

print('')

http_get = requests.get(url)
print(http_get.text)

####################################################
print('\n\n')
print("=" * 50)
