from django.urls import path
from .views import (DirectorList, DirectorDetail, MovieList, MovieDetail,
                    ReviewList, ReviewDetail, MoviesWithReviews, DirectorsWithMoviesCount)

urlpatterns = [
    path('api/v1/directors/', DirectorList.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', DirectorDetail.as_view(), name='director-detail'),
    path('api/v1/movies/', MovieList.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', MovieDetail.as_view(), name='movie-detail'),
    path('api/v1/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetail.as_view(), name='review-detail'),
    path('api/v1/movies/reviews/', MoviesWithReviews.as_view(), name='movies-with-reviews'),
    path('api/v1/directors/movies_count/', DirectorsWithMoviesCount.as_view(), name='directors-with-movies-count'),
]
