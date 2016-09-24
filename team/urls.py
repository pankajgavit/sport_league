from django.conf.urls import url
from .  import views

app_name = 'team'


urlpatterns = [
    #/team/
    url(r'^$',views.index, name='index' ),

    #/team/
]
