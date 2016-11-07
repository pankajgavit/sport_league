from django.db import models
#BLUE PRINT OF THE DATABASE
# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    logo = models.FileField()
    wins = models.IntegerField()
    ties = models.IntegerField()
    loss = models.IntegerField()
    points = models.IntegerField()
    runrate = models.FloatField()

    def matches_(self):
        if self.id:
            return self.wins + self.loss + self.ties

    matches = property(matches_) #wins + loss + ties

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=250)
    DOB = models.DateField()
    Role = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_image = models.FileField()
    goals = models.IntegerField(default = 0)
    assists = models.IntegerField(default = 0)
    yellow_card = models.IntegerField(default = 0)
    red_card = models.IntegerField(default = 0)
    Rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.player_name


class Coach(models.Model):
    coach_name = models.CharField(max_length=250)
    DOB = models.DateField()
    coach_team = models.ForeignKey(Team,on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    coach_image = models.FileField()

    def __str__(self):
        return self.coach_name












