from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sofo_name = models.CharField(max_length=50, unique=True, verbose_name='sofo 닉네임')

    def __str__(self):
        return self.sofo_name

    @property
    def average_rating(self):
        return round(self.user.review_set.aggregate(Avg('rating'))['rating__avg'], 1)

    class Meta:
        db_table = 'profiles'





