from django.db import models

# Create your models here.

class Transfer (models.Model):
    name = models.CharField(max_length=250)
    kit = models.FileField()
    price = models.CharField(max_length=250)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

