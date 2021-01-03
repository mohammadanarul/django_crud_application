from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default='writing your blog content....')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}-{self.created_at}'
    