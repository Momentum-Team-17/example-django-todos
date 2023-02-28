from django.shortcuts import render
from .forms import ItemForm
from .models import Item

# Create your views here.
# our functions will mostly go here


def list_todos(request):
    todos = Item.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})


def create_todo(request):
    form = ItemForm()
    return render(request, 'todos/new_todo.html', {'form': form})
