from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# Create your views here.
# our functions will mostly go here


def list_todos(request):
    todos = Item.objects.all()
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
