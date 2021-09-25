from django.db import models

# Create your models here.
class Atracao(models.Model):
  nome = models.CharField(
    verbose_name="Nome",
    max_length=150
  )

  descricao = models.TextField(
    verbose_name="Descricao"
  )

  horario_func = models.TextField(
    verbose_name="Horario de funcionamento"
  )

  idade_minima = models.IntegerField(
    verbose_name="Idade Mínima"
  )

  def __str__(self) -> str:
      return self.nome