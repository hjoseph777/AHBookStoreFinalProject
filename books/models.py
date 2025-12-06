from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    # Basic book info - keeping it simple for now
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)  # might add validation here later
    year = models.IntegerField()  # TODO: might want to add validation later
    rating = models.FloatField()  # out of 5 stars
    description = models.TextField()
    
    # Track who added this book - useful for edit permissions
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # Just return the title - keeps things clean
        return self.title

    def get_absolute_url(self):
        # Django convention for getting the detail view URL 
        return reverse('book_detail', kwargs={'pk': self.pk})