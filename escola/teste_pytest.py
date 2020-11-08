import requests

class TestCurso:
  headers = { "Authorization": "Token b45bb4512c74946db1e875a24c477b8606078f26"}
  url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

  #the name of method has to be test_<name>
  def test_get_cursos(self):
    cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

    assert cursos.status_code == 200

  def test_get_curso(self):
    curso = requests.get(url=f'{self.url_base_cursos}10/', headers=self.headers)

    assert curso.status_code == 200

  def test_post_curso(self):
    novo = {
      "titulo": "Programming Python4",
      "url": "http://www.propython4.com"
    }

    resposta = requests.post(
      url=self.url_base_cursos, 
      headers=self.headers, 
      data=novo
    )

    assert resposta.status_code == 201
    assert resposta.json()['titulo'] == novo['titulo']

  def test_put_curso(self):
    atualizado = {
      "titulo": "New Programming Course52",
      "url": "http://www.googlenewprogrammingcourse52.com.br"
    }

    resposta = requests.put(
      url=f'{self.url_base_cursos}7/', 
      headers=f'{self.headers}', 
      data=atualizado)

    assert resposta.status_code == 200
    # assert resposta.json()['titulo'] == atualizado['titulo']

  def test_put_titulo_curso(self):
    atualizado = {
      "titulo": "New Programming Course63",
      "url": "http://www.googlenewprogrammingcourse63.com.br"
    }

    resposta = requests.put(
      url=f'{self.url_base_cursos}8/', 
      headers=f'{self.headers}', 
      data=atualizado)

    assert resposta.json()['titulo'] == atualizado['titulo']

  def test_delete_curso(self):
    resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)

    assert resposta.status_code == 204 and len(resposta.text) == 0
