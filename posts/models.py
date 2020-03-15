from django.db import models

from django.utils import timezone


class Post(models.Model):

    text = models.TextField(verbose_name='post')

    def __str__(self):
        """Representation model as string"""
        return self.text[:50]
