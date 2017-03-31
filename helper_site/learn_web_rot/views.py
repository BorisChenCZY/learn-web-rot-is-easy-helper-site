from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get(request):
    if request.GET:
        s = ''
        for key, value in dict(request.GET).items():
            s += '{} = {} <br>'.format(key, value)
        return HttpResponse(s)
    else:
        return HttpResponse('you didn\' send anything to this website')
def index(request):
    return render(request, 'learn_web_rot/home.html')
