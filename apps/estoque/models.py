from django.db import models
from util.models import Cidade


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    class Meta:
        # https://docs.djangoproject.com/en/1.10/ref/models/options/#unique-together
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return "{n}".format(n=self.nome)

class Fabricante(models.Model):
    nome = models.CharField(max_length=64)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=256)
    cidade = models.ForeignKey(Cidade)

    class Meta:
        # https://docs.djangoproject.com/en/1.10/ref/models/options/#unique-together
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"

    def __str__(self):
        return "{n}".format(n=self.nome)


class Marca(models.Model):
    nome = models.CharField(max_length=64)
    fabricante = models.ForeignKey(Fabricante)

    class Meta:
        unique_together = ('nome', 'fabricante')
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
    
    def __str__(self):
        return "{n}".format(n=self.nome)
        
class Produto(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    nome = models.CharField(max_length=64)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return "{n}".format(n=self.nome)