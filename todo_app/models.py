from django.db import models


# User model for assignee details
class User(models.Model):
    assignee_name = models.CharField(
        max_length=100, null=True, blank=True
    )  # Assignee name
    email = models.EmailField()  # Assignee email

    def __str__(self):
        return (
            self.assignee_name
        )  # Display the assignee name in the admin panel or string representation


# Task model with both ForeignKey and a string field for arbitrary assignee names
class Task(models.Model):
    CHOICES = [
        ("urgent", "Urgent"),
        ("epic", "Epic"),
        ("normal", "Normal"),
        ("low", "Low Priority"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # Optional description
    status = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    typex = models.CharField(max_length=20, choices=CHOICES, default="normal")
    email = models.EmailField(
        null=True, blank=True
    )  
    
    assignee_name = models.CharField(
        max_length=100, null=True, blank=True
    )  # Allow any string value

    def __str__(self):
        return (
            self.title
        )  # Display the task title in the admin panel or string representation
