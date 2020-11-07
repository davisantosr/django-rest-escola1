from rest_framework import serializers
from django.db.models import Avg #class to get Average
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
    #pattern validate_<field name>
  def validate_avaliacao(self, valor):
    if valor in range(1, 6):
      return valor
    raise serializers.ValidationError('Avaliação precisa ser inteiro de 1 a 5')
  


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

  media_avaliacoes = serializers.SerializerMethodField()

  class Meta:
    model = Curso
    fields = (
      'id',
      'titulo',
      'url',
      'criacao',
      'ativo',
      'avaliacoes',
      'media_avaliacoes',
    )

  def get_media_avaliacoes(self, obj):
    media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

    if media is None:
      return 0
    return round(media * 2)/2  #To round number
