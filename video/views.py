from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Videos

def index(request):
    all_videos = Videos.objects.all()
    return render(request, 'videos/index.html',{'all_videos' : all_videos})
