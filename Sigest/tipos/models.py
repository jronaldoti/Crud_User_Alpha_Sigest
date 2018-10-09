from django.db import models

class Tipo(models.Model):
    tarefa = models.CharField(max_length=40)
    descricao = models.TextField(max_length=400)

    def __str__(self):
        return self.tarefa