from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list }
    return render(request, 'first_app/index.html', context=date_dict)


def indexUser(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'user_records': user_list }
    return render(request, 'first_app/users.html', context=user_dict)

def test(request):
    return HttpResponse("<h1>Test</h1>")
