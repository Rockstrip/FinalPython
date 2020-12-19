from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Artur, hi!")


def index2(request):
    return HttpResponse("Sasha, PRIVET!")