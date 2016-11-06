from django.db import models
from team.models import Team
#BLUE PRINT OF THE DATABASE
# Create your models here.

class Matches(models.Model):
    home = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name="home")
    away = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name="away")
    # 0 - Upcoming, 1 - proper result, 2 - tied
    result = models.IntegerField(default=0)
    result_team = models.ForeignKey('team.Team', on_delete=models.CASCADE, related_name="match_result", null="False")
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)
    video = models.CharField(max_length=2000, null=True)

    def __str__(self):
        #if the home team and away team are same
        '''if(self.away_id==self.home_id):
            return 'Same teams cannot play against each other..!! Are you kidding me..? '

        #selecting a result not in home and away
        if(self.result_id!=self.home_id and self.result_id!=self.away_id) :
            return 'The result entered is not from the given options, Please enter a valid option.. Come on man..!! Youre a grown up now'

        won = Team.objects.get(pk=self.result_id)
        lost = Team.objects.get(pk=self.away_id)
        if(self.result_id==self.away_id):
            lost = Team.objects.get(pk=self.home_id)

        #incrementing the wins and losses
        won.matches = int(won.matches)+1
        lost.matches = int(lost.matches)+1
        won.save()
        lost.save()'''

        #Matches.objects.filter(pk=self.result_id).update(home='jdflksjldf')

        return str(self.home.team_name) + " vs " + str(self.away.team_name)