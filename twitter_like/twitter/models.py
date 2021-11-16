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
    author = models.ForeignKey('User',
                               on_delete=models.SET_NULL,
                               null=True,
                               default="User Deleted")
    content = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author}'

    def to_dict(self):
        object_as_dict = {
            'title': self.title,
            'author': self.author.name,
            'pub_date': str(self.pub_date)
        }

        return object_as_dict
