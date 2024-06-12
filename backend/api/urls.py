from django.urls import path
from . import views 

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('get', views.getEmployee, name="getEmployee"),
    path('add', views.addEmployee, name="addEmployee"),
]
