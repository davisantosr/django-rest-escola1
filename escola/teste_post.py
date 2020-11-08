import requests

headers = {"Authorization": "Token b45bb4512c74946db1e875a24c477b8606078f26"}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
  "titulo": "Programming Py",
  "url": "http://www.google1.com.br"
}

resultado = requests.post(url_base_cursos, headers=headers, data=novo_curso)

#Testado o código de status HTTP
print(resultado.json())
assert resultado.status_code == 201

#Testando se o curso retornado é o mesmo do informado

assert resultado.json()['titulo']==novo_curso['titulo']