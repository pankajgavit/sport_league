from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Team

def index(request):
    all_teams = Team.objects.all()
    return render(request, 'team/index.html',{'all_teams' : all_teams})

def detail(request, team_id):
    return HttpResponse("<h1>Details of team id :" + str(team_id)+ " </h1>")