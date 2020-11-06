from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

  class Meta:
    
    #extra parameter. Email will be able just for write
    extra_kwargs = {
      'email': {'write_only': True}
    }
    model = Avaliacao
    fields = (
      'id',
      'curso', 
      'nome',
      'email',
      'comentario',
      'avaliacao',
      'criacao',
      'ativo',
    )


class CursoSerializer(serializers.ModelSerializer):
  '''
  NESTED RELATIONSHIP
  Show the relationship between avaliacoes and cursos

  avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

  HYPERLINKED RELATED FIELD
  create a hyperlink to the data(its own link for endpoint)

  avaliacoes = serializers.HyperlinkedRelatedField(
    many=True, read_only=True, view_name='avaliacao-detail')

  PRIMARY KEY RELATED
  show the objects related's primary key
'''

  avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Curso
    fields = (
      'id',
      'titulo',
      'url',
      'criacao',
      'ativo',
      'avaliacoes',
    )