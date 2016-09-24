from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, get_object_or_404
#from .models import Team

def index(request):
  #  all_teams = Team.objects.all()
    return render(request, 'team/index.html')
