from django.http import HttpResponse
def home(request):
    return HttpResponse("This is my HomePage")
def contact(request):
    return HttpResponse("This is contact")