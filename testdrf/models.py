from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ("Pending", 'Pending'),
        ("In Progress", 'In Progress'),
        ("Completed", 'Completed')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='Pending')
    due_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}--{self.tittle}'