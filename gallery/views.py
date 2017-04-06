from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Gallery

def index(request):
    all_gallery = Gallery.objects.order_by('image_team')
    return render(request, 'gallery/index.html',{'all_gallery': all_gallery})




