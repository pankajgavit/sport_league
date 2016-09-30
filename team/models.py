from django.db import models
#BLUE PRINT OF THE DATABASE
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    logo = models.FileField()
    rank = models.IntegerField()
    matches =  models.IntegerField()
    wins = models.IntegerField()
    ties = models.IntegerField()
    loss = models.IntegerField()
    points = models.IntegerField()


    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_name = models.CharField(max_length=250)
    DOB = models.DateField()
    Role = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_image = models.FileField()

    def __str__(self):
        return self.player_name





