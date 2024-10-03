from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


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
