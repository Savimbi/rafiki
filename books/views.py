from django.shortcuts import render
from .models import BookTitle
from django.shortcuts import render 

def book_title_list_view(request):
    qs = BookTitle.objects.all()
    return render(request, "books/main.html", {"qs":qs})


def book_title_detail(request,pk):
    qs = BookTitle.objects.get(pk=pk)
    return render(request, "books/detail.html", {'book':qs})

