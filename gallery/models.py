from django.db import models
#BLUE PRINT OF THE DATABASE
# Create your models here.


class Gallery(models.Model):
    gallery = models.FileField()
    image_info = models.CharField(max_length=50)

    def __str__(self):
        return self.image_info