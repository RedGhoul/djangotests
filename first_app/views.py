from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.forms import FormName, NewUser, UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone Tried to Login and Failed")
            print(username)
            print(password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



@login_required
def register(request):
    registered = False
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # not saving the form the sec we get it or we might create another user
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    return render(request, 'first_app/register.html', context=context_dict)

# Create your views here.
def index_form(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    form_dict = {'form': form}
    return render(request, 'first_app/formname.html', context=form_dict)


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

    return render(request, 'first_app/createuser.html', context=form_dict)


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list,
                 'text': 'this is some text',
                 'number': 330304304}
    return render(request, 'first_app/index.html', context=date_dict)


def indexUser(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'user_records': user_list}
    return render(request, 'first_app/users.html', context=user_dict)


def test(request):
    return HttpResponse("<h1>Test</h1>")
