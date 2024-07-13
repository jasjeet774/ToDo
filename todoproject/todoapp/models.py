from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    Date=models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
