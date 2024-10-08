from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(default=None, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
