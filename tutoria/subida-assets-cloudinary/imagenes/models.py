from django.db import models

# Create your models here.
#DENTRO DE LOS MODELS SIEMPRE VA LAS TABLAS

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    img_url =models.ImageField(upload_to='images/', blank=True, null=True)
    imge_url_full = models.URLField(blank=True, null=True)
