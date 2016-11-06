from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


from .utils import generic_search
from team.models import Team, Player, Coach
from django.shortcuts  import render_to_response,redirect

QUERY="search-query"

MODEL_MAP = { Team: ["team_name",],
                 Player  : ["player_name"],
                 Coach : ["coach_name"]

   }

def search(request):
       objects = []

       for model,fields in MODEL_MAP.iteritems():

           objects+=generic_search(request,model,fields,QUERY)

       return render_to_response("search_results.html",
                                 {"objects":objects,
                                  "search_string" : request.GET.get(QUERY,""),
                              }
       )