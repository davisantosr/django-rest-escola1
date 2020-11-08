import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v1/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota)

# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

notas = jsonpath.jsonpath(avaliacoes.json(),'results[*].avaliacao')
print(notas)
