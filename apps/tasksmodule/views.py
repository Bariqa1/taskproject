from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasksmodule/list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        status = request.POST['status']

        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            status=status,
        )
        
        return redirect('task_list')

    return render(request, 'tasksmodule/add.html')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.priority = request.POST['priority']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()
        
        return redirect('task_list')

    return render(request, 'tasksmodule/edit.html', {'task': task})

def task_details(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasksmodule/details.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    # لو GET → اعرض صفحة التأكيد
    if request.method == "GET":
        return render(request, 'tasksmodule/delete.html', {'task': task})

    # لو POST → احذف المهمة
    task.delete()
    return redirect('task_list')

