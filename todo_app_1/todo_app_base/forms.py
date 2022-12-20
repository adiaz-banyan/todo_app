from django import forms
from django.db.utils import IntegrityError

from todo_app_base.models import Task, Comment, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {"description": forms.TextInput(attrs={"size": 80})}

        fields = ["description"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        task_object = kwargs.pop("task_object")
        super().__init__(*args, **kwargs)

        self.instance.task = task_object
        self.fields["body"].label = ""
