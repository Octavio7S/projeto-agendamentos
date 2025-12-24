from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    nome_servico = models.CharField(max_length=20)
    duracao = models.IntegerField()

    def __str__(self):
        return self.nome_servico


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()

#    def __str__(self):
#        return self.servico