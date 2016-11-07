from django.conf.urls import url
from .  import views

app_name = 'matches'


urlpatterns = [
    #/matches/
    url(r'^$', views.index, name='index'),

    #/matches/fixtures/
    url(r'^fixtures', views.fixtures, name='fixtures'),

    #matches/broadcast/
    url(r'^broadcast', views.broadcast, name='broadcast'),
]
