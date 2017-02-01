from django.contrib import admin
from . models import Fabricante, Marca, Produto, Categoria

class MarcaInline(admin.TabularInline):
    model=Marca

class FabricanteInline(admin.TabularInline):
    model=Fabricante

class ProdutoInline(admin.TabularInline):
    model=Produto


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fabricante']
    inlines = [ProdutoInline]

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'endereco']
    inlines = [MarcaInline]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'marca']
    list_filter = ['marca', 'marca__fabricante']
# Register your models here.

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria)
