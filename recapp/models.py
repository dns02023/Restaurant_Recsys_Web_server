from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=50)
    place_location = models.CharField(max_length=100)
    place_tags = models.TextField()

    def __str__(self):
        return self.place_name

    @property
    def average_rating(self):
        return round(self.review_set.aggregate(Avg('rating'))['rating__avg'], 1)

    class Meta:
        db_table = 'places'

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    #null, blank 조건을 통해 null값 또는 아예 폼에서 입력을 안하는 것을 허용


    class Meta:
        db_table = 'reviews'

