from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive number.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'movie', 'stars']

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Review text cannot be empty.")
        return value
