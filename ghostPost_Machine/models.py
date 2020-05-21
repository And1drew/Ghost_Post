from django.db import models
from django.utils import timezone


class BoastOrRoast(models.Model):
    description = models.TextField(default='boast or roast something here')
    isBoast = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    vote_score = models.IntegerField()

    def __str__(self):
        return self.description
