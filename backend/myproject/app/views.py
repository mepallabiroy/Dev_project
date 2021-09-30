from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from .models import Person
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Welcome to my 1st development Project !!!")

def getjson(request):
    if(request.method == 'GET'):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def person_details(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)
