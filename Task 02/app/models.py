from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")])
    due_date = models.DateField(blank=True, null=True)  # New field
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
