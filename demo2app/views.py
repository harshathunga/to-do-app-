from django.forms.forms import Form
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from matplotlib.style import context
import demo2app
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import *
from .form import *
from demo2app import form
# Create your views here.


def tas(request):
    tasks = Task.objects.all()

    form = Taskforms()
    contex = {"tasks":tasks, "form":form} 

    return render(request, 'demo2app/oop.html',contex )


def ho(request):

    tasks = Task.objects.all()

    form = Taskforms()
    if request.method == 'POST':
        form  = Taskforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    contex = {"tasks":tasks, "form":form} 
    return render(request, 'demo2app/uh.html', contex )


def upadatetask(request, pk):
    

    task = Task.objects.get(id=pk)
    form = Taskforms(instance=task)
    if request.method == "POST":
        form  = Taskforms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    

    return render(request, "demo2app/update_task.html", context)

def deletetask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task': task}

    return render(request, "demo2app/delete.html", context)