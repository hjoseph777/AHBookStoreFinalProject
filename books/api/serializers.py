from rest_framework import serializers
from ..models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'rating', 'description']  # excluding user for API
        # NOTE: not exposing user info through the API for privacy