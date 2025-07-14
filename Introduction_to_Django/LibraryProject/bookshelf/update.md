## update operations
'''python
book=Book.objects.filter(pk=2).update(title="Nineteen Eighty-Four")
print(book.title)
 
 Output:Nineteen Eighty-Four