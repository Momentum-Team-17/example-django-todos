from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item

# Create your views here.
# our functions will mostly go here


def list_todos(request):
    todos = Item.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})


def get_todo_by_priority(request, priority):
    todos = Item.objects.filter(priority=priority)
    return render(request, 'todos/index.html', {'todos': todos})


def create_todo(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        # form bound with data (filled out)
        if item_form.is_valid():
            # django checks if all the form data is valid
            item_form.save()
            # this saves a new instance of Item in the database using the form data. This works because we are inheriting from ModelForm
            return redirect('home')
    form = ItemForm()
    return render(request, 'todos/new_todo.html', {'form': form})


def detail_todo(request, pk):
    # takes in pk value from url
    # todo = Item.objects.get(pk=pk)
    # the line above with throw an error if there is no item with that pk in the database, so we use get_object_or_404
    todo = get_object_or_404(Item, pk=pk)
    # get the Item object whose primary key matches pk that was passed in the url
    return render(request, 'todos/detail_todo.html', {'todo': todo})


def edit_todo(request, pk):
    todo = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, instance=todo)
        if item_form.is_valid():
            item_form.save()
            return redirect('home')
    form = ItemForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'pk': pk})


def delete_todo(request, pk):
    todo = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        todo.delete()
    return render(request, 'todos, delete_todo.html')
