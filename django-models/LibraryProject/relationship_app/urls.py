from .views import books_list
from django.urls import path
from .views import LibraryDetailView
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    

]