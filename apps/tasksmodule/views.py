from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasksmodule/list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        task_type = request.POST['task_type']
        status = request.POST['status']

        due_time = request.POST.get('due_time')
        due_date_raw = request.POST.get('due_date')

        if task_type == "Specific" and due_date_raw:
            due_date = due_date_raw
        else:
            due_date = None

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            task_type=task_type,
            due_date=due_date,
            due_time=due_time,
            status=status
        )

        return redirect('/')

    return render(request, "tasksmodule/add.html")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.task_type = request.POST.get('task_type')
        task.due_time = request.POST.get('due_time')

        if request.POST.get('task_type') == 'Specific':
            task.due_date = request.POST.get('due_date')
        else:
            task.due_date = None 

        task.save()

        return redirect('task_list') 

    return render(request, 'tasksmodule/edit.html', {'task': task})


def task_details(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasksmodule/details.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "GET":
        return render(request, 'tasksmodule/delete.html', {'task': task})

    task.delete()
    return redirect('task_list')

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.status = "Completed"
    task.save()
    return redirect('/')
