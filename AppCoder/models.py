from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hospedaje(models.Model):
    
    nombre=models.CharField(max_length=40)
    HabDispo=models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Habitaciones disponibles: {self.HabDispo}"

class huesped(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

"""class reserva(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrada= models.DateField()
    pagado= models.BooleanField()"""

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True,blank=True)

