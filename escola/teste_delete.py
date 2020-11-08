import requests

headers = {"Authorization": "Token b45bb4512c74946db1e875a24c477b8606078f26"}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

#Teste de código HTTP
assert resultado.status_code == 204

#Teste se o tamanho do conteudo retorno é 0 
assert len(resultado.text) == 0