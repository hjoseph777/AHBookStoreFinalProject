from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='api_get_books'),
    path('books/<int:pk>/', views.get_book, name='api_get_book'),
]