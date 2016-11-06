from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Team, Player

def index(request):
    all_teams = Team.objects.all()
    return render(request, 'team/index.html',{'all_teams' : all_teams})


def detail(request, team_id):
    team = Team.objects.get(pk=team_id)
    return render(request, 'team/player.html',{'team': team})

def standings(request):
    all_teams = Team.objects.all()
    return render(request, 'team/standings.html',{'all_teams' : all_teams})

def stats(request, team_id, player_id):
    player = Player.objects.get(pk=player_id)
    team = Team.objects.get(pk=team_id)
    return render(request, 'team/player_stats.html', {'player': player,'team': team})




