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
        ('implante', 'implante'),
        ('canal', 'canal')
    )
    firstname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    achado01 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado02 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado03 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado04 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado05 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado06 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado07 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado08 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado09 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado10 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado11 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado12 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado13 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado14 = models.CharField(max_length=20, choices=PATHOLOGY)
    achado15 = models.CharField(max_length=20, choices=PATHOLOGY)
    img=models.ImageField(upload_to='detection')


    def __str__(self):
        return self.firstname