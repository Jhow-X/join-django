from django.contrib import admin
from .models import Alvo

# Registrando o modelo Alvo no painel administrativo
@admin.register(Alvo)
class AlvoAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'nome', 'latitude', 'longitude', 'data_expiracao')
    search_fields = ('nome', 'identificador')
    list_filter = ('data_expiracao',)

