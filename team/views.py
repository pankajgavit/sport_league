from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Coach
from matches.models import Matches

def index(request):
    all_teams = Team.objects.all()
    return render(request, 'team/index.html',{'all_teams' : all_teams})


def detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team/player.html',{'team': team})


def standings(request):
    update(Matches.objects.all())
    all_teams = Team.objects.all().order_by('-points')
    return render(request, 'team/standings.html',{'all_teams' : all_teams})


def statistics(request):
    all_player_goals = Player.objects.order_by('-goals')[:20]
    all_player_assists = Player.objects.order_by('-assists')[:20]
    all_player_yellow = Player.objects.order_by('-yellow_card')[:20]
    all_player_red = Player.objects.order_by('-red_card')[:20]
    return render(request, 'team/statistics.html',{'all_player_goals' : all_player_goals, 'all_player_assists' : all_player_assists,
                                                  'all_player_yellow': all_player_yellow,'all_player_red' : all_player_red})


def coach(request):
    all_coach = Coach.objects.order_by('coach_team')
    return render(request, 'team/coach.html',{'all_coach' : all_coach})


def stats(request, team_id, player_id):
    player = Player.objects.get(pk=player_id)
    team = Team.objects.get(pk=team_id)
    return render(request, 'team/player_stats.html', {'player': player,'team': team})

#updates the team stats
def update(all_matches):
    for teams in Team.objects.filter():
        Team.objects.filter(pk=teams.id).update(wins=0,loss=0,ties=0,points=0,runrate=0)

    for matches in all_matches:    
        # proper result
        if (matches.result == 1):
            # winning and losing goals
            if (matches.result_team == matches.home):
                winning_goals = matches.home_goals
                losing_goals = matches.away_goals
            else:
                winning_goals = matches.away_goals
                losing_goals = matches.home_goals
    
            # winning team
            updated_wins = matches.result_team.wins + 1
            updated_points = 3*matches.result_team.wins + matches.result_team.ties
            updated_run_rate = matches.result_team.runrate + (winning_goals - losing_goals)
            Team.objects.filter(pk=matches.result_team.id).update(wins=updated_wins,
                                                                points=updated_points,
                                                                runrate=updated_run_rate)

            if (matches.result_team == matches.home):
                losing_team = matches.away
            else:
                losing_team = matches.home
    
            # losing team
            updated_loss = losing_team.loss + 1
            updated_run_rate = losing_team.runrate - (winning_goals - losing_goals)
            Team.objects.filter(pk=losing_team.pk).update(loss=updated_loss,
                                                          runrate=updated_run_rate)
    
        elif (matches.result == 2):
            # home team
            updated_ties = matches.home.ties + 1
            updated_points = 3 * matches.home.wins + matches.home.ties
            updated_run_rate = matches.home.runrate + matches.home_goals
            Team.objects.filter(pk=matches.home.id).update(ties=updated_ties,
                                                            points=updated_points,
                                                            runrate=updated_run_rate)

            # away team
            updated_ties = matches.away.ties + 1
            updated_points = 3 * matches.away.wins + matches.away.ties
            updated_run_rate = matches.away.runrate + matches.home_goals
            Team.objects.filter(pk=matches.away.id).update(ties=updated_ties,
                                                            points=updated_points,
                                                            runrate=updated_run_rate)
    points_update(Team.objects.all())
    return

def points_update(all_teams):
    for team in all_teams:
        update_points = 3 * team.wins + team.ties
        Team.objects.filter(pk=team.pk).update(points=update_points)


def contact(request):
    return render(request,'team/contact.html')


def insti(request):
    return render(request,'team/institutional.html')


