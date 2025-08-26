from .views import books_list
from django.urls import path
from .views import LibraryDetailView
from .views import register,login_view,logout_view


urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', register(), name='register'),
    path('login/', login_view(), name='login'),
    path('logout/', logout_view(), name='logout'),
    

]