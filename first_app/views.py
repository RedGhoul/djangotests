from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from first_app.forms import FormName, NewUser
# Create your views here.
def index_form(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    form_dict = {'form':form}
    return render(request,'first_app/formname.html',context=form_dict)

def create_user_form(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            # we can save the data here directly since
            # we are using a model form
            form.save(commit=True)
            return indexUser(request)
        else:
            print('Error Form invalid')

    form_dict = {'form': form}

    return render(request,'first_app/createuser.html',context=form_dict)

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
