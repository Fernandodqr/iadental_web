from django.db import models

# Create your models here.
class Detection(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Famale', 'Famale')
    )
    PATHOLOGY = (
        ('restauração', 'restauracao'),
        ('coroa', 'coroa'),
        ('implante', 'implante')
    )
    firstname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    achado01 = models.CharField(max_length=20, choices=PATHOLOGY)
    img=models.ImageField(upload_to='detection')


    def __str__(self):
        return self.firstname