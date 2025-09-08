from django.shortcuts import render
from django.http import JsonResponse
from models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)