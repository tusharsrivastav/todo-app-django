from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TodoForm()
        todos = Todo.objects.order_by('completed', '-date_created')
        context = {'todos' : todos, 'form' : form}

        return render(request, 'todos/index.html', context)

def delete(request, todo_id):
    todo_to_dlt = get_object_or_404(Todo, id=todo_id)
    todo_to_dlt.delete()
    return redirect('home')

def cross_off(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def uncross(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('home')

def dlt_completed(request):
    todos_to_dlt = Todo.objects.filter(completed=True)
    todos_to_dlt.delete()
    return redirect('home')
