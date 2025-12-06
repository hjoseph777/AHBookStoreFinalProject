from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Homepage showing all books - pretty straightforward
class BookListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'  # makes template cleaner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = 'AH Bookstore'  # branding for the header
        return context

# Individual book details page
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'
    # Django handles everything else automatically

# Adding new books - only logged in users can do this
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/form.html'
    extra_context = {'title': 'Add Book'}
    
    def form_valid(self, form):
        # Make sure we track who added this book
        form.instance.user = self.request.user
        return super().form_valid(form)

# Edit existing books - but only if you own them
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm  
    template_name = 'books/form.html'  # reuse the same form template
    extra_context = {'title': 'Edit Book'}
    
    def test_func(self):
        # Only the person who added the book can edit it
        current_book = self.get_object()
        return self.request.user == current_book.user
    
    def handle_no_permission(self):
        # Friendly error message when someone tries to edit someone else's book
        messages.error(self.request, "You can only edit books that you added.")
        return redirect('book_detail', pk=self.get_object().pk)

# Delete functionality - same ownership rules apply
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/confirm_delete.html'
    success_url = reverse_lazy('index')  # back to homepage after delete
    
    def test_func(self):
        book = self.get_object()
        return self.request.user == book.user
    
    def handle_no_permission(self):
        messages.error(self.request, "You can only delete books that you added.")
        return redirect('book_detail', pk=self.get_object().pk)

# User registration - pretty standard Django stuff
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'books/auth_form.html', {'form': form, 'title': 'Register'})

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('index')
    return render(request, 'books/auth_form.html', {'form': form, 'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('login')  # send them back to login page