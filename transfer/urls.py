from django.conf.urls import url
from . import views

app_name = 'transfer'


urlpatterns = [
    #/transfer/
    url(r'^$',views.index, name='index' ),

    ]