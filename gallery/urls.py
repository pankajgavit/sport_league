from django.conf.urls import url
from . import views

app_name = 'gallery'


urlpatterns = [
    #/gallery/
    url(r'^$',views.index, name='index' ),

    ]