from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def index(request):
    todos = TodoItem.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)

def delete_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    todo.delete()
    return redirect('index')
