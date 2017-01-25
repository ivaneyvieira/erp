from django.db import models

# Create your models here.
class Regiao(models.Model):
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=2, unique=True)
    def __str__(self):
        return "{sg} - {nm}".format(sg=self.sigla, nm=self.nome)

class Estado(models.Model):
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    def __str__(self):
        return "{sg} - {nm}".format(sg=self.sigla, nm=self.nome)
