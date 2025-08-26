from .views import books_list
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    

]