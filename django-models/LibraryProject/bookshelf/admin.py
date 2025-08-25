from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these columns in the admin listing
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search box that searches title and author
    search_fields = ('title', 'author')
