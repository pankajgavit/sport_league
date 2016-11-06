from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Coach

def index(request):
    all_teams = Team.objects.all()
    return render(request, 'team/index.html',{'all_teams' : all_teams})


def detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team/player.html',{'team': team})


def standings(request):
    all_teams = Team.objects.all()
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





