from django.contrib import admin
from books.models import books, ReviewBooks, Tag, Book

admin.site.register(books)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(ReviewBooks)