from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=300)
    data = models.CharField(max_length=300)
    local = models.CharField(max_length=400)
    cartaz = models.FileField(default='/inicial/static/img/logo.png')
    tickets = models.CharField(max_length=1000)
    evento_face = models.CharField(max_length=1000)
    descricao = models.TextField(max_length=10000)
    fotos = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome

