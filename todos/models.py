from django.db import models

# Create your models here.
# our classes will mostly go here
# docs about model fields https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types


class Item(models.Model):
    # inherits from django's built in Model class
    # choosing a field type makes the data more predictable
    # fields are required by default
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    # database puts a timestamp when an item is created
    priority = models.PositiveIntegerField()
    description = models.TextField()
    is_hidden = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} | priority: {self.priority}'
