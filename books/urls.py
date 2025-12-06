from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('add/', views.BookCreateView.as_view(), name='add_book'),
    path('edit/<int:pk>/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('api/', include('books.api.urls')),
]