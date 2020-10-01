from django.shortcuts import render, redirect
from .models import task
from .forms import task_form
# Create your views here.

def home(request):
    forms = task_form()
    tasks = task.objects.all()
    if request.method == 'POST':
        form = task_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'forms':forms}
    return render(request, 'home.html', context)


def update(request, pk):
    tasks = task.objects.get(id = pk)
    form = task_form(instance=tasks)
    if request.method == 'POST':
        form = task_form(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'update_page.html', context)


def delete(request, pk):
    tasks = task.objects.get(id=pk)
    if request.method == "POST":
        tasks.delete()
        return redirect('/')

    return render(request, 'delete_page.html', {'tasks':tasks})