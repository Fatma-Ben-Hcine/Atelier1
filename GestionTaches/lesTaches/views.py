from django.http import HttpResponse  
from lesTaches.models import Task # import de la class Task 
from django.shortcuts import render # import de la methode render 
from django.template import Template,Context  
from rest_framework import viewsets 
from .models import Task 
from .serializers import TaskSerializer 
 
def home(request): 
    return HttpResponse('bonjour à tous') 
 
def task_listing(request): 
    tasks  =  Task.objects.all().order_by('due_date') 
 
 
    return render(request,template_name='list.html',context={'tasks':tasks}) 
 
class TaskViewSet(viewsets.ModelViewSet): 
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer 