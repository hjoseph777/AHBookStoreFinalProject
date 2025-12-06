from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(request):
    """Return all books in JSON format - pretty straightforward"""
    book_list = Book.objects.all()  # maybe should add some filtering later
    serializer = BookSerializer(book_list, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, pk):
    """Get a single book by its ID"""
    try:
        book_item = Book.objects.get(pk=pk)
        serializer = BookSerializer(book_item)
        return Response(serializer.data)
    except Book.DoesNotExist:
        # Return proper 404 when book doesn't exist
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)