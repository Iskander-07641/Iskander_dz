from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.db.models import Avg
from django.db.models import Count


class DirectorList(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)


class DirectorDetail(APIView):
    def get(self, request, id):
        try:
            director = Director.objects.get(pk=id)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)


class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetail(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetail(APIView):
    def get(self, request, id):
        try:
            review = Review.objects.get(pk=id)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


class MoviesWithReviews(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        data = []
        for movie in movies:
            reviews = Review.objects.filter(movie=movie)
            avg_rating = reviews.aggregate(Avg('stars'))['stars__avg']
            data.append({
                'movie': MovieSerializer(movie).data,
                'reviews': ReviewSerializer(reviews, many=True).data,
                'rating': avg_rating
            })
        return Response(data)


class DirectorsWithMoviesCount(APIView):
    def get(self, request):
        directors = Director.objects.annotate(movies_count=Count('movies'))

        data = []
        for director in directors:
            data.append({
                'director': DirectorSerializer(director).data,
                'movies_count': director.movies_count
            })
        return Response(data)