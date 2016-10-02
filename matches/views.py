from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Matches

def index(request):
    all_matches = Matches.objects.all()
    return render(request, 'matches/matches_index.html',{'all_matches' : all_matches})
