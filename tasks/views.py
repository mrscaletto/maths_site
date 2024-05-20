from django.shortcuts import render
from tasks.models import Task

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    if request.method == 'POST':
        user_answers = {key: request.POST[key] for key in request.POST.keys() if key.startswith('answer_')}
        results = {task.id: (str(user_answers.get(f'answer_{task.id}')) == str(task.answer)) for task in tasks}
        context['results'] = results
    return render(request, 'task_list.html', context)

