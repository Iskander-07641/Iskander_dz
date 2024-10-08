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

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorDetail(APIView):
    def get(self, request, id):
        try:
            director = Director.objects.get(pk=id)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            director = Director.objects.get(pk=id)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            director = Director.objects
            director.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            movie = Movie.objects
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(request, id):
    try:
        review = Review.objects.get(pk=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ReviewDetail(APIView):
    def get(self, request, id):
        try:
            review = Review.objects.get(pk=id)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            review = Review.objects.get(pk=id)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
