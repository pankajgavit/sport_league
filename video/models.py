from django.db import models
#BLUE PRINT OF THE DATABASE
# Create your models here.

class Videos(models.Model):
    video_title = models.CharField(max_length=100)
    youtube_embedded_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.video_title