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


class Lote(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    data_validade = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return "{n} - {p}".format(n=self.codigo, p=self.produto)


class Prateleira(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Prateleira"
        verbose_name_plural = "Prateleiras"

    def __str__(self):
        return "{n} - {p}".format(n=self.codigo, p=self.categoria)


class Estoque(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=15, decimal_places=4)
    prateleira = models.ForeignKey(Prateleira, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lote', 'prateleira')
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"

    def __str__(self):
        return "{l} - {p}".format(l=self.lote, p=self.prateleira)

    def adcionar(self, quant):
        self.quantidade += quant

    def subtrair(self, quant):
        self.quantidade -= quant
