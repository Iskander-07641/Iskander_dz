from django.urls import path
from .views import (
    DirectorList, DirectorDetail,
    MovieList, MovieDetail,
    ReviewList, ReviewDetail,
    MoviesWithReviews, DirectorsWithMoviesCount,
    UserRegistrationView, UserConfirmationView
)

urlpatterns = [
    path('directors/', DirectorList.as_view(), name='director-list'),
    path('directors/<int:id>/', DirectorDetail.as_view(), name='director-detail'),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieDetail.as_view(), name='movie-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewDetail.as_view(), name='review-detail'),
    path('movies/reviews/', MoviesWithReviews.as_view(), name='movies-with-reviews'),
    path('directors/count/', DirectorsWithMoviesCount.as_view(), name='directors-with-count'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('confirm/', UserConfirmationView.as_view(), name='user-confirmation'),
]
