# from common.models import Tag
from django.db import models


class Right(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    text = models.TextField()
    color = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    # tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
