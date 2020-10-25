from django.http import HttpResponse

def www(request):
    return HttpResponse("WWW")

def api(request):
    return HttpResponse("API")
