from django.conf.urls import url
from first_app import views
from django.urls import path
# got to set "app_name" to something
# before you can use relative paths in your templates
app_name = 'first_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register,name='register'),
    path('login', views.user_login,name='login'),
    path('formname', views.index_form,name='formname'),
    path('createuser', views.create_user_form,name='createuser'),
    path('users', views.indexUser, name='user'),
    path('test', views.test, name='test'),
]
