from django.urls import path
from . import views 

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('get/', views.getEmployee, name="getEmployee"),
    path('add/', views.addEmployee, name="addEmployee"),
    path('put/', views.putEmployee, name="putEmployee"),
    path('patch/', views.patchEmployee, name="patchEmployee"),
    path('delete/', views.deleteEmployee, name="deleteEmployee"),
]
