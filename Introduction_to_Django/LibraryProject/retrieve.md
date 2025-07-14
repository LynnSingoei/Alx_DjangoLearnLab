## Retrieve operation
'''python 
retrieved = Book.objects.get(pk=2)
print(retrieved.title, retrieved.publication_year)

Output: 1984 1949