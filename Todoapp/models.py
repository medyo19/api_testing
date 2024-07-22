from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_items')

    def __str__(self):
        return self.title