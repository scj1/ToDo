from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect(
                "home"
            )  # Redirect to home or any other page after registration
    else:
        form = UserRegistrationForm()
    return render(request, "todo_app/register.html", {"form": form})


@login_required
def index(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Save form data to variables
            task_title = form.cleaned_data["title"]
            task_description = form.cleaned_data["description"]
            assignee_name = form.cleaned_data["assignee_name"]
            email = form.cleaned_data["email"]
            task_deadline = form.cleaned_data.get("deadline")
            typex = form.cleaned_data["type"]

            print(
                f"Task: {task_title}, Description: {task_description}, Assignee: {assignee_name}, Email: {email}, Deadline: {task_deadline}, Type: {typex}"
            )
            form.save()
            return redirect("home")  # Redirect to home page

    tasks = Task.objects.all()  # Fetch all tasks from the database
    context = {"tasks": tasks, "form": form}
    return render(request, "todo_app/index.html", context)


def updateTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = True
    task.save()
    return redirect("home")


def deleteTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect("home")


def viewTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {"task": task}
    return render(request, "todo_app/view.html", context)


def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()  # Save the new task to the database

            # Send email
            subject = "New Task Added"
            message = f"Task Name: {task.title}\nDescription: {task.description}\nAssignee Name: {task.assignee_name}\nAssignee Email: {task.email}\nDeadline date: {task.deadline}\nType: {task.typex}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [task.email]  # Send email to the assignee

            send_mail(subject, message, from_email, recipient_list)

            return redirect("home")
    else:
        form = TaskForm()

    return render(request, "todo_app/add.html", {"form": form})
