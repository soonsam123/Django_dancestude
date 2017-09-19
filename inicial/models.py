from django.db import models

class Parceiro(models.Model):
    nome = models.CharField(max_length=300)
    local = models.CharField(max_length=300)
    logo = models.FileField(default='inicial/static/img/logo.png')
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome
