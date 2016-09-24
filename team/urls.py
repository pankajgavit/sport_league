from django.conf.urls import url
from .  import views

app_name = 'team'


urlpatterns = [
    #/team/
    url(r'^$',views.index, name='index' ),

    #/team/712/
    url(r'^(?P<team_id>[0-9]+)/$', views.detail , name='detail'),
]
