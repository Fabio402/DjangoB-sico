from django.db import models
from django.db.models.deletion import DO_NOTHING


class Cargos(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Pessoas(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargos, DO_NOTHING)

    def __str__(self):
        return self.name
    

