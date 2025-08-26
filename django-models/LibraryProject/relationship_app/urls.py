from .views import books_list, Library_view
from django.urls import path

urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', Library_view.as_view(), name='library_detail'),

]