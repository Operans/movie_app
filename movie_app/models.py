from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.review.all().count()

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'stars': i.stars} for i in reviews]

    @property
    def avg_reviews(self):
        reviews = Review.objects.filter(movie=self)
        res = [int(i.stars) for i in reviews]

        return round(sum(res) / len(res))

class Review(models.Model):

    stars = models.CharField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return self.movie.title

