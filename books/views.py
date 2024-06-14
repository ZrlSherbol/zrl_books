from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from random import randint
from books.models import books
from . import forms

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
        sort = request.GET.get("sort")
        if sort == 'date_of_creation':
            query = books.objects.filter().order_by('date_of_creation')
        else:
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

def edit_book_view(request, id):
    book_id = get_object_or_404(books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book successfully updated!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='blog/edit_book.html',
                  context={
                      'form': form,
                      'book_id': book_id
                  })

def drop_book_view(request, id):
    book_id = get_object_or_404(books, id=id)
    book_id.delete()
    return HttpResponse('book deleted <a href="/books/">На список книг</a>')


def create_book_view(request):
    if request.method == "POST":
        form = forms.book_id(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>book successfully created!</h3>'
                                '<a href="/books/">На список книг</a>')
    else:
        form = forms.book_id()

    return render(request, template_name='blog/create_book.html',
                  context={'form': form})