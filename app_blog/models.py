from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    brief = models.CharField(max_length=140)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    comment = models.TextField()
    STATUS = (
        (0, 'Filtrado'),
        (1, 'Permitido'),
    )
    status = models.CharField(choices=STATUS, max_length=10, default='Filtrado')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
