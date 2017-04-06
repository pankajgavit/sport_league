from django.db import models
#BLUE PRINT OF THE DATABASE
# Create your models here.


class Gallery(models.Model):
    gallery = models.FileField()
    image_info = models.CharField(max_length=50)
    image_team = models.CharField(max_length=100,default="madrid")

    def __str__(self):
        return self.image_info