from . import views
from django.urls import path

urlpatterns=[
path("",views.register,name='register'),
path("work",views.work,name='work'),
path("login",views.login,name='login'),
]