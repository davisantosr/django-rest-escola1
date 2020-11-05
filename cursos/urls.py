from django.urls import path

from .views import CursoAPIView, CursosAPIView, AvaliacaoAPIView, AvaliacoesAPIView
urlpatterns = [
  path('cursos/', CursosAPIView.as_view(), name='cursos'),
  path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
  path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view()),
#<int:curso_pk> tell to developer which pk we are setting
  path('cursos/<int:curso_pk>avaliacoes/<int:avaliacao_pk/', AvaliacaoAPIView.as_view(), name='curso_avaliacao')

  path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
  path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

]
