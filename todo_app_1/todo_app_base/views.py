from django.shortcuts import redirect, render
from django.views import View
from todo_app_base.forms import TaskForm, CommentForm
from todo_app_base.models import Task, Comment

# Create your views here.
class HomeView(View):
    def get(self, request):
        task_form = TaskForm()
        tasks = Task.objects.all()

        html_data = {"tasks": tasks, "form": task_form}

        return render(request=request, template_name="index.html", context=html_data)

    def post(self, request):
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect("home")


class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)

        task_form = TaskForm(instance=task)

        comments = Comment.objects.filter(task=task)
        comment_form = CommentForm(task_object=task)

        html_data = {
            "task_object": task,
            "form": task_form,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(request=request, template_name="detail.html", context=html_data)

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)

        if "update" in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()

        elif "delete" in request.POST:
            task.delete()

        elif "add" in request.POST:
            comment_form = CommentForm(request.POST, task_object=task)
            comment_form.save()

            return redirect("task_detail", task.id)

        return redirect("home")
