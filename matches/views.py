from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Matches

def index(request):
    all_matches = Matches.objects.all()
    return render(request, 'matches/index.html',{'all_matches' : all_matches})

def fixtures(request):
    all_matches = Matches.objects.all()
    return render(request, 'matches/fixtures.html',{'all_matches' : all_matches})

def broadcast(request):
    all_matches = Matches.objects.filter(result=3)
    if len(all_matches) == 1:
        return render(request, 'matches/broadcast.html', {'all_matches': all_matches})
    elif len(all_matches) == 0:
        return render(request, 'matches/no_broadcast.html', {'all_matches': all_matches})