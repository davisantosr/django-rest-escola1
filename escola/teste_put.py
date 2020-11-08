import requests

headers = {"Authorization": "Token b45bb4512c74946db1e875a24c477b8606078f26"}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
  "titulo" : "Testing Method Put",
  "url": "https://www.testing.com.br"
}

resultado = requests.get(
  url=f'{url_base_cursos}2/', 
  headers=headers, 
)

# print(resultado.json())

# resultado = requests.put(
#   url=f'{url_base_cursos}2/', 
#   headers=headers, 
#   data=curso_atualizado
# )

# #Testando status HTTP
# assert resultado.status_code == 200

# #Testando o titulo
# assert resultado.json()['titulo'] == curso_atualizado['titulo']

print(resultado.json())