''' 
Mateus Israel, 7 de novembro de 2018
Consumindo APIs com python
Exemplo 1:
'''

import requests                                                    # Biblioteca requests

cep = str(input('Cep: '))                                          # Vamos pegar o cep por input
url_endereco = 'https://viacep.com.br/ws/' + cep + '/json/'        # Formatando a url passando o cep por parametro
print('GET para: ' + url_endereco)                                # Simplesmente para ter um feedback do endereço(URL)

print('')

http_get = requests.get(url_endereco)                              # Vamos fazer uma requisição para a url que editamos
print(http_get.text)                                               # printando o GET com a formatação .text, ou seja, JSON