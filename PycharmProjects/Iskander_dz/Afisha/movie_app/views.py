from django.db.models import Avg, Count
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from movie_app.db_connection import get_connection


from .models import Director, Movie, Review, User
from .serializers import (DirectorSerializer,
                          MovieSerializer,
                          ReviewSerializer,
                          UserRegistrationSerializer,
                          UserConfirmationSerializer)


class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MoviesWithReviews(generics.ListAPIView):
    def get_queryset(self):
        return Movie.objects.prefetch_related('reviews').annotate(avg_rating=Avg('reviews__stars'))

    def list(self, request, *args, **kwargs):
        movies = self.get_queryset()
        data = []
        for movie in movies:
            data.append({
                'movie': MovieSerializer(movie).data,
                'reviews': ReviewSerializer(movie.reviews.all(), many=True).data,
                'rating': movie.avg_rating
            })
        return Response(data)


class DirectorsWithMoviesCount(generics.ListAPIView):
    def get_queryset(self):
        return Director.objects.annotate(movies_count=Count('movies'))

    def list(self, request, *args, **kwargs):
        directors = self.get_queryset()
        data = []
        for director in directors:
            data.append({
                'director': DirectorSerializer(director).data,
                'movies_count': director.movies_count
            })
        return Response(data)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UserConfirmationView(generics.CreateAPIView):
    serializer_class = UserConfirmationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            try:
                user = User.objects.get(username=username)
                user.is_active = True
                user.confirmation_code = ""
                user.save()
                return Response({"message": "User confirmed successfully."}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def my_view(request):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM your_table;")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return JsonResponse(results, safe=False)
