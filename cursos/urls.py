from django.urls import path

from .views import CursoApiView, AvaliacaoAPIView

urlpatterns = [
  path('cursos/', CursoApiView.as_view(), name='cursos'),
  path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]