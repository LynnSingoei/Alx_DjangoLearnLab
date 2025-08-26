from django.shortcuts import HttpResponse
from .models import Book

# Create your views here.
def books_list(request):
    books=Book.objects.all()
    output=""
    for book in books:
        output += f"Title: {book.title}, Author: {book.author.name}<br>"
    return HttpResponse(output)

class Library_view(DetailView):
    model=Library

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context