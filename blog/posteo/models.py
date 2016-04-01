from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=40)
    contenido=models.TextField()
    estampaInicial=models.DateTimeField(auto_now=False,auto_now_add=True)
    estampaActualizacion=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicodde__(self):
        return self.titulo
