from django.shortcuts import render , redirect
from django.http import HttpResponse
from todolist_app.models import Todolist
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
        messages.success(request , "New Task Added")

        return redirect("todolist")
    else:
        all_tasks = Todolist.objects.filter(manage = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get("pg")
        all_tasks = paginator.get_page(page)
        return render (request ,"todolist.html" ,{'all_tasks': all_tasks})

@login_required
def task_delete(request , task_id):
    task = Todolist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messagess.error(request , "Access Restricted, You Are Not Allowed")
    return redirect("todolist")

@login_required
def edit_task(request , task_id):
    if request.method =="POST":
        task = Todolist.objects.get(pk = task_id)
        form = TaskForm(request.POST or None  , instance =task)
        if form.is_valid():
            form.save() 
        messages.success(request , "Task Edited")

        return redirect("todolist")
    else:
        task_obj = Todolist.objects.get(pk = task_id)
        return render (request ,"edit.html" ,{'task_obj': task_obj})

@login_required
def task_complete(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messagess.error(request , "Access Restricted, You Are Not Allowed")
    return redirect("todolist")

@login_required
def pending_task(request , task_id):
    task = Todolist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect("todolist")

def contact(request):
    context= {"contact": "welcome to contact "}
    return render (request ,"contact.html" , context)

def aboutus(request):
    
    return render (request ,"aboutus.html")

def homepage(request):
    context = {"home": "welcome to homepage "}
    return render (request ,"homepage.html" , context)

    