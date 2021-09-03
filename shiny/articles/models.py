from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#inherits from model class
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # add an author later
    # this fuction controls how the object looks, to show the title of every object when you retrive from the DB
    def __str__(self):
       return self.title
    def snippet(self):
        return self.body[:50]+'...'
