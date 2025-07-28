from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Pareja(models.Model):
    solicitante = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="parejas_solicitadas")
    numero_pareja = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    miembro_1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='parejas_como_1', on_delete=models.CASCADE)
    miembro_2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='parejas_como_2', on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    es_fake = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)



