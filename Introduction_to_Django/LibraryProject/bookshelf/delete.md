## delete operations
from bookshelf.models import Book
Book.objects.filter(pk=2).delete()
Output: (1, {'bookshelf.Book': 1})