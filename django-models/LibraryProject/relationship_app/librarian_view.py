from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import is_librarian

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")