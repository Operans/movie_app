from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.get_list_of_directors, name='get_list_of_directors'),
    path('api/v1/directors/<int:director_id>/', views.director_detail, name='director_detail'),
    path('api/v1/movies/', views.get_list_of_movies, name='get_list_of_movies'),
    path('api/v1/movies/<int:movie_id>/', views.moive_detail, name='moive_detail'),
    path('api/v1/reviews/', views.get_list_of_reviews, name='get_list_of_reviews'),
    path('api/v1/reviews/<int:review_id>/', views.reviews_detail, name='reviews_detail'),
]