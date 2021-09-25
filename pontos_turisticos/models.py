from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
# Create your models here.
class PontoTuristico(models.Model):
  nome = models.CharField(
    verbose_name="Nome",
    max_length=150
  )

  descricao = models.TextField(
    verbose_name="Descrição"
  )

  aprovado = models.BooleanField(default=False)

  atracoes = models.ManyToManyField(Atracao)

  comentarios = models.ManyToManyField(Comentario)

  avaliacoes = models.ManyToManyField(Avaliacao)

  def __str__(self) -> str:
      return self.nome