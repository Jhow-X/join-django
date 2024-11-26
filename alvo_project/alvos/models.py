from django.db import models

class Alvo(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_expiracao = models.DateField()

    def __str__(self):
        return self.nome
