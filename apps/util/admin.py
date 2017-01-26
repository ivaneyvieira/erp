from django.contrib import admin
from . models import Estado, Regiao, Cidade
# Register your models here.


admin.site.register(Regiao)
admin.site.register(Estado)
admin.site.register(Cidade)
