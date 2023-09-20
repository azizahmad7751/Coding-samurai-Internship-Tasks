from django.shortcuts import render,redirect
from .models import Task
from django.views.decorators.http import require_POST
from django.http import JsonResponse

@require_POST
def add_task(request):
    title = request.POST['title']
    description = request.POST['description']
    priority = request.POST['priority']
    due_date = request.POST.get('due_date', None)  # Optional due date
    task = Task(title=title, description=description, priority=priority, due_date=due_date)
    task.save()
    return redirect('task-list')


def update_task_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.completed = not task.completed  # Toggle status
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        return JsonResponse({'status': 'success'})
    except Task.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Task not found'})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})
