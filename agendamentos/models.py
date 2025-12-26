from django.db import models

# Create your models here.

class Barbearia(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    

class Barbeiro(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        on_delete=models.CASCADE,
        related_name="barbeiros"
    )
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        on_delete=models.CASCADE,
        related_name="servicos"
    )
    nome = models.CharField(max_length=100)
    duracao_minutos = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        on_delete=models.CASCADE,
        related_name="agendamentos"
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="agendamentos"
    )
    barbeiro = models.ForeignKey(
        Barbeiro,
        on_delete=models.CASCADE,
        related_name="agendamentos"
    )
    servico = models.ForeignKey(
        Servico,
        on_delete=models.PROTECT
    )
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("agendado", "Agendado"),
            ("confirmado", "Confirmado"),
            ("cancelado", "Cancelado"),
            ("finalizado", "Finalizado"),
        ],
        default="agendado"
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.data} {self.hora_inicio}"