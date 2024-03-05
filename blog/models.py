from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # need to import timezone from django.utils
    date = models.DateTimeField(default=timezone.now)
    # one user can have multiple posts , we use a foreign key

    # if a user is deleted the post is deleted as well due to the on_delete= models.CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
