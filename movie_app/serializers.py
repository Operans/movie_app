from rest_framework import serializers
from .models import Director, Movie, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DirectorSerializer(serializers.ModelSerializer):
    count_of_movie = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name count_of_movie'.split()

    def get_count_of_movie(self, director):
        return director.movie_set.count()



class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title director category reviews count_reviews all_reviews'.split()

    def get_category(self, movie):
        try:
            return movie.category.name
        except:
            return 'No category'

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(author__isnull=False, movie=movie),
                                      many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id text rate_stars author movie'
