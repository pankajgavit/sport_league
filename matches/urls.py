from django.conf.urls import url
from .  import views

app_name = 'matches'


urlpatterns = [
    #/team/
    url(r'^$', views.index, name='index'),

]
