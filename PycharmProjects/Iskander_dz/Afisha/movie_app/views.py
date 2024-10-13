from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.db.models import Avg, Count


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
    def get_object(self, id):
        try:
            return Director.objects.get(pk=id)
        except Director.DoesNotExist:
            raise Http404

    def get(self, request, id):
        director = self.get_object(id)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, id):
        director = self.get_object(id)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        director = self.get_object(id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    def get_object(self, id):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ReviewDetail(APIView):
    def get_object(self, id):
        try:
            return Review.objects.get(pk=id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, id):
        review = self.get_object(id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, id):
        review = self.get_object(id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        review = self.get_object(id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesWithReviews(APIView):
    def get(self, request):
        movies = Movie.objects.prefetch_related('reviews').annotate(avg_rating=Avg('reviews__stars'))
        data = []
        for movie in movies:
            data.append({
                'movie': MovieSerializer(movie).data,
                'reviews': ReviewSerializer(movie.reviews.all(), many=True).data,
                'rating': movie.avg_rating
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
