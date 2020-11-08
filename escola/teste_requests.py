import requests

#GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# #Acessando código de status http
# print(avaliacoes.status_code)

# #Acessando dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

#Acessando quantidade de registros
# print(avaliacoes.json()['count'])

#Acessando a proxima página de resultados
# print(avaliacoes.json()['next'])

#Acessando resultado desta página
# print(avaliacoes.json()['results'])

#Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

#Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

#Acessando o nome da pessoa que avaliou a ultima avaliacao
# print(avaliacoes.json()['results'][-1]['nome'])

#GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/6/')
# print(avaliacao.json())

# GET Cursos 
headers = {'Authorization': 'Token b45bb4512c74946db1e875a24c477b8606078f26'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())



