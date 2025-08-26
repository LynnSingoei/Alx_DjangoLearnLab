from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import is_member

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")