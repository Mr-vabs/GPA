from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=200)
