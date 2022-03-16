from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=200, default="")
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Todo #{}'.format(self.id)
