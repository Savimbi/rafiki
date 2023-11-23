from django.contrib import admin

from books.models import Book, BookTitle

admin.site.register(Book)
admin.site.register(BookTitle)
