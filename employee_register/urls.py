from django.urls import path, include
from .import  views

urlpatterns = [
    path(' ', views.emloyee_form) ,
    path('list/',  views.employee_list)
]