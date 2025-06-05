from django.shortcuts import render
from .models import Task, TaskCategory
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

@login_required
def task_category_list(request):
    categories = TaskCategory.objects.all()
    return render(request, 'task/task_category_list.html', {'categories': categories})
