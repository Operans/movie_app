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

    @property
    def count_movies(self):
        return self.movies.all().count()


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
        return self.reviews.all().count()

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]


class Review(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')

    def __str__(self):
        return self.movie.title
