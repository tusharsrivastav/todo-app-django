from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text", "completed"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['todo_text'].widget.attrs.update({
                                                    'class': 'create_bar',
                                                    'placeholder': 'Add a new task',
                                                })
