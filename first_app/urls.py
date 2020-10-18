from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('formname', views.index_form,name='formname'),
    path('createuser', views.create_user_form,name='createuser'),
    path('users', views.indexUser, name='user'),
    path('test', views.test, name='test'),
]
