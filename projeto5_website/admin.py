from django.contrib import admin
from projeto5_website.models import Pergunta, Alternativa, Teste, Resultado, Aluno, Turma

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'dominancia', 'cautela', 'estabilidade', 'influencia', 'resultado_final', 'instituicao')
    list_filter = ('aluno', 'resultado_final', 'instituicao')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'email', 'instituicao')
    list_filter = ('ra', 'nome', 'email', 'instituicao')

admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Teste)
admin.site.register(Resultado, ResultadoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma)