from . import views
from .views import books_list
from django.urls import path
from .views import LibraryDetailView

from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', views.register, name='register'),
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
    path('admin/dashboard/', views.admin_view,name='admin_view'),
    path('librarian/dashboard/', views.librarian_view,name='librarian_view'),
    path('member/dashboard/', views.member_view,name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),


    

]