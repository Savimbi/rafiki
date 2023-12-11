from django.urls import path

from .views import book_title_list_view, book_title_detail


app_name = "books"

urlpatterns = [
    path("", book_title_list_view),
    path("<pk>",book_title_detail),
]