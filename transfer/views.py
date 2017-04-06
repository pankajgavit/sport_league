from django.shortcuts import render
from .models import Transfer

# Create your views here.

def index(request):
    all_teams = Transfer.objects.all()
    return render(request, 'transfer/index.html',{'all_teams' : all_teams})
