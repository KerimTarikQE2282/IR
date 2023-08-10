from django.http import JsonResponse
from .Something import somethins
from django.http import HttpResponse
from rest_framework.decorators import api_view



@api_view(['POST'])
def index(request):
    my_query=request.data['query']['Querys']
    people = somethins.get_people(my_query)
    return  JsonResponse(people,safe=False)
    return  JsonResponse(people,safe=False)




