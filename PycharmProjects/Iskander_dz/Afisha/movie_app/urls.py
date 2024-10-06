from django.urls import path
from .views import (DirectorList, DirectorDetail, MovieList,
                    MovieDetail, ReviewList, ReviewDetail, MoviesWithReviews,
                    DirectorsWithMoviesCount)

urlpatterns = [
    path('directors/', DirectorList.as_view()),
    path('directors/<int:id>/', DirectorDetail.as_view()),
    path('movies/', MovieList.as_view()),
    path('movies/<int:id>/', MovieDetail.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:id>/', ReviewDetail.as_view()),
    path('movies/reviews/', MoviesWithReviews.as_view()),
    path('directors/movies_count/', DirectorsWithMoviesCount.as_view()),
]
