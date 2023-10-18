from django.contrib import admin

# Register your models here.
from .models import Categoria, TipoAtuacao, Pais, Produtora, Membro, Filme, Atuacao

class AtuacaoInline(admin.TabularInline):
    model = Atuacao

admin.site.register(Categoria)
admin.site.register(TipoAtuacao)
admin.site.register(Pais)
admin.site.register(Produtora)
admin.site.register(Atuacao)

@admin.register(Filme)

class FilmeAdmin(admin.ModelAdmin):
    inlines = [AtuacaoInline]

@admin.register(Membro)

class MembroAdmin(admin.ModelAdmin):
    inlines = [AtuacaoInline]