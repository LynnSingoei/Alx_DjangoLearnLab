from LibraryProject.bookshelf import views
from .views import books_list
from django.urls import path
from .views import LibraryDetailView

from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', views.Registerview, name='register'),
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
    

]