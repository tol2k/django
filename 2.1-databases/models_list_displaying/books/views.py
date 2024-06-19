from django.shortcuts import render
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def book_view(request,slug):
    template = 'books/book.html'
    context = {'book': Book.objects.get(slug=slug)}
    return render(request, template, context)