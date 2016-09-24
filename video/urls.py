from django.conf.urls import url
from .  import views

urlpatterns = [
    #/videos/
    url(r'^$',views.index, name='index' ),

    #/videos/
]
