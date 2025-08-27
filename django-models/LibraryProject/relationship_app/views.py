from django.shortcuts import HttpResponse
from .models import Book
from .models import Library
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def books_list(request):
    books=Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model=Library
    template_name="relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
    


def login_view(request):
    return render(request, 'relationship_app/login.html')


def logout_view(request):
    return render(request, 'relationship_app/logout.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")