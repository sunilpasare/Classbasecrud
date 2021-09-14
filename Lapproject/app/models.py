from django.db import models

class Laptop(models.Model):
    Modelname=models.CharField(max_length=20)
    Company=models.CharField(max_length=20)
    Ram=models.FloatField()
    Rom=models.FloatField()
    Weight=models.FloatField()
    Processor=models.CharField(max_length=5)

    

