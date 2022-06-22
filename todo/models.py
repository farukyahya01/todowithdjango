from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    class StatusChoices(models.TextChoices):
        active = 'active',
        in_progress = 'in_progress',
        done = 'done',
        passive = 'passive',
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.active)
    expected_end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

