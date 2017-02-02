from django.contrib import admin
from . models import Fabricante, Marca, Produto, Categoria, Estoque, Lote, Prateleira


class MarcaInline(admin.TabularInline):
    model = Marca


class FabricanteInline(admin.TabularInline):
    model = Fabricante


class ProdutoInline(admin.TabularInline):
    model = Produto


class LoteInline(admin.TabularInline):
    model = Lote
class EstoqueInline(admin.TabularInline):
    model = Estoque
######################################################################


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fabricante']
    inlines = [ProdutoInline]


class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'endereco']
    inlines = [MarcaInline]


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'marca']
    list_filter = ['marca', 'marca__fabricante']
    inlines = [LoteInline]
    search_fields = ['codigo', 'nome']


class LoteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'data_validade', 'produto']
    inlines=[EstoqueInline]


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['lote', 'quantidade', 'prateleira']


class PrateleiraAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'categoria']
    inlines=[EstoqueInline]
# Register your models here.

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Lote, LoteAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Prateleira, PrateleiraAdmin)
