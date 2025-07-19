from django.db import models
from django.contrib.auth.models import User

class Pareja(models.Model):
    numero_pareja = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    miembro_1 = models.ForeignKey(User, related_name='parejas_como_1', on_delete=models.CASCADE)
    miembro_2 = models.ForeignKey(User, related_name='parejas_como_2', on_delete=models.CASCADE)
