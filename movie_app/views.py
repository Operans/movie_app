from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSer, MovieSer, ReviewSer
from rest_framework import status

@api_view(['GET'])
def get_list_of_directors(request):
    directors = Director.objects.all()
    data = DirectorSer(directors, many=True).data
    return Response(data)

@api_view(['GET'])
def director_detail(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Режиссер не найден"})
    data = DirectorSer(director).data
    return Response(data=data)

@api_view(['GET'])
def get_list_of_movies(request):
    movies = Movie.objects.all()
    data = MovieSer(movies, many=True).data
    return Response(data)

@api_view(['GET'])
def moive_detail(request, movie_id):
    try:
        movies = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Movie не найден"})
    data = MovieSer(movies).data
    return Response(data=data)

@api_view(['GET'])
def get_list_of_reviews(request):
    reviews = Review.objects.all()
    data = ReviewSer(reviews, many=True).data
    return Response(data)

@api_view(['GET'])
def reviews_detail(request, review_id):
    try:
        reviews = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Review не найден"})
    data = ReviewSer(reviews).data
    return Response(data=data)