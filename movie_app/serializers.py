from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
