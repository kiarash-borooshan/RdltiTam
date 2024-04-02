from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def y(self, year):
        return self.filter(publish__year=year)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=60)
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

    objects = PostManager()
    published = PublishedManager()

    def __str__(self):
        return self.title
