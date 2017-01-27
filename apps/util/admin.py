from django.contrib import admin
from . models import Estado, Regiao, Cidade
# Register your models here.


class AdminRegiao(admin.ModelAdmin):
    list_display=['nome', 'sigla']


admin.site.register(Regiao, AdminRegiao)
admin.site.register(Estado)
admin.site.register(Cidade)
