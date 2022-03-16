from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo_text', 'completed')

admin.site.register(Todo, TodoAdmin)
