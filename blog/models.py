from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="blog_post")
    body = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default="Draft")
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)
