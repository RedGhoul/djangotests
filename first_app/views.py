from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hellp i am trying to get out of the machine"}
    return render(request, 'first_app/index.html', context=my_dict)


def test(request):
    return HttpResponse("<h1>Test</h1>")
