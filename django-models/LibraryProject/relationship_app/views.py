from django.shortcuts import HttpResponse
from .models import Book

# Create your views here.
def books_list(request):
    books=Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})

class Library_view(DetailView):
    model=Library
    template_name="relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context