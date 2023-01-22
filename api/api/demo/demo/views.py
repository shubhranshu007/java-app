import json
from django.http import HttpResponse, JsonResponse
def cities_population(request):
    response_data = {}
    response_data['city'] = 'Agra'
    response_data['population'] = '7lakh'
    return JsonResponse(response_data, safe=False)