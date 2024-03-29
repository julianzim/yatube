from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date_published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    