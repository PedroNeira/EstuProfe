from django.db import models

# Create your models here.

class User(models.Model):
    
    firstName = models.CharField(max_length=32, verbose_name= "Nombre")
    lastName = models.CharField(max_length=32, verbose_name= "Apellido")
    birthdate = models.DateField( verbose_name= "Fecha de Nacimiento")
    gender = models.CharField(max_length=30, verbose_name= "Genero")
    phoneNumber =  models.IntegerField( verbose_name= "Telefono")
    educationLevel = models.CharField(max_length=32, verbose_name= "Nivel Educativo")
    email =  models.EmailField()
    password = models.CharField(max_length=32, verbose_name= "Constraseña")

class Publication(models.Model):
   
    publicationDate = models.DateTimeField(auto_now_add = True, verbose_name= "Fecha Publicacion")
    deadline =models.DateTimeField(auto_now_add= True, verbose_name= "No se")
    area =models.CharField(max_length=32, verbose_name= "Area de Conocimiento")
    description =  models.TextField(max_length=100, verbose_name= "Descripcion")
    isAccepted = models.BooleanField()

class Tutorship(models.Model):
    
    userTutorId = models.IntegerField()
    userStudentId = models.IntegerField()
    tutorShipDate = models.DateTimeField()
    hour = models.CharField(max_length=10)

