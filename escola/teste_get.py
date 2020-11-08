import requests

headers = {"Authorization": "Token b45bb4512c74946db1e875a24c477b8606078f26"}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/' 

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

#Testando se o endpoint está correto

# assert resultado.status_code == 200
# #testando elemento de resultado
# assert resultado.json()['count'] == 5

assert resultado.json()['results'][0]['titulo'] == 'Curso1'