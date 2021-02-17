from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 30)
    # pictures = models.ImageField()
    content = models.TextField()
    date = models.DateTimeField(auto_now = True)
    slug = models.SlugField(null = True, unique = True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    content = models.TextField()

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
#     pictures = models.ImageField()
#     content = models.CharField(max_length = 200)