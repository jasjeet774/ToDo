from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm


def redirect_to_admin_login(request):
    return redirect('/admin/login/?next=/')



@login_required
def index(request):
    todos = TodoItem.objects.filter(user=request.user)
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('index')
    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)


def delete_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    todo.delete()
    return redirect('index')
