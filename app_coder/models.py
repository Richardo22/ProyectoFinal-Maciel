from django.db import models

# Create your models here.
class Empanada(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre}-{self.ingredientes}-{self.precio}'          
    

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.nombre}-{self.ingredientes}-{self.precio}'
    
    

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.nombre}-{self.ingredientes}-{self.precio}'
    
    

