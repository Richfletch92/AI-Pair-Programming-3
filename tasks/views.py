from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm
import json

def task_list(request):
    if request.method == 'POST':
        if 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect('task_list')
        else:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
    else:
        form = TaskForm()

    todo_tasks = Task.objects.filter(completed=False).order_by('-due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('-due_date')
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        completed = data.get('completed', False)
        try:
            task = Task.objects.get(id=task_id)
            task.completed = completed
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})