from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi, I'm back!")