from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.register(Item)
# register each model here once on its own line
# makes Django Admin aware of our model
