from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=60)
    pub_date = models.DateTimeField(default=timezone.now)
    _author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author}'

    @property
    def author(self):
        if not self._author:
            return 'User Deleted'
        return self._author

