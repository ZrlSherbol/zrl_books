from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from random import randint
from books.models import books

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Моё имя: Шербол"
                        "\nФамилия: Орозов"
                        "\nвозрост: 16 лет")
def my_hobby(request):
    if request.method == 'GET':
        return HttpResponse("я увлекаюсь программированием внутренней части сайтов."
                        "направление: BACKEND")

def Time(request):
    if request.method == 'GET':
        return HttpResponse(f"{datetime.datetime.now()}")

def random(request):
    if request.method == 'GET':
        return HttpResponse(f"Рандомное чилсо: {randint(1, 1000)}")

def books_list_view(request):
    if request.method == 'GET':
        query = books.objects.filter().order_by('-id')
        return render(
            request,
            template_name='blog/book_list.html',
            context={
                'books': query
            }
        )

def books_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(books, id=id)
        return render(
            request,
            template_name='blog/book_detail.html',
            context={
                'book': book_id
            }
        )

def all_books(request):
    if request.method == 'GET':
        books = books.objects.filter().order_by('-id')
        return render(request, template_name='products/all_products.html',
                      context={'books': books})


def for_book_view(request):
    if request.method == 'GET':
        book = books.objects.filter(tags__name='Еда').order_by('-id')
        return render(request, template_name='products/for_eat_view.html',
                      context={
                          'book': book
                      })