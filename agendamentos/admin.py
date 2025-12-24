from django.contrib import admin
from .models import Cliente, Servico, Agendamento

# Register your models here.
@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    ...

@admin.register(Servico)
class AdminServico(admin.ModelAdmin):
    ...

@admin.register(Agendamento)
class AdminAgendamento(admin.ModelAdmin):
    ...