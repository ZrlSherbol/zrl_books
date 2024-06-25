from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from django.views import generic
from random import randint
from books.models import books
from . import forms


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Моё имя: Шербол" "\nФамилия: Орозов" "\nвозрост: 16 лет")


def my_hobby(request):
    if request.method == "GET":
        return HttpResponse(
            "я увлекаюсь программированием внутренней части сайтов."
            "направление: BACKEND"
        )


def Time(request):
    if request.method == "GET":
        return HttpResponse(f"{datetime.datetime.now()}")


def random(request):
    if request.method == "GET":
        return HttpResponse(f"Рандомное чилсо: {randint(1, 1000)}")


# def books_list_view(request):
#     if request.method == 'GET':
#         sort = request.GET.get("sort")
#         if sort == 'date_of_creation':
#             query = books.objects.filter().order_by('date_of_creation')
#         else:
#             query = books.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='blog/book_list.html',
#             context={
#                 'books': query
#             }
#         )


class BooksListView(generic.ListView):
    template_name = "blog/book_list.html"
    context_object_name = "books"
    model = books
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        pass


# def books_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(books, id=id)
#         return render(
#             request,
#             template_name='blog/book_detail.html',
#             context={
#                 'book': book_id
#             }
#         )


class BooksDetailView(generic.DetailView):
    template_name = "blog/book_detail.html"
    context_object_name = "book_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(books, id=book_id)


# def edit_book_view(request, id):
#     book_id = get_object_or_404(books, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book successfully updated!</h3>'
#                                 '<a href="/books/">На список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, template_name='blog/edit_book.html',
#                   context={
#                       'form': form,
#                       'book_id': book_id
#                   })


class EditBookView(generic.UpdateView):
    template_name = "blog/edit_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get("id")
        return get_object_or_404(books, id=emp_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


# def drop_book_view(request, id):
#     book_id = get_object_or_404(books, id=id)
#     book_id.delete()
#     return HttpResponse('book deleted <a href="/books/">На список книг</a>')


class DeleteBookView(generic.DeleteView):
    template_name = "blog/delete_book.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(books, id=book_id)


# def create_book_view(request):
#     if request.method == "POST":
#         form = forms.book_id(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>book successfully created!</h3>'
#                                 '<a href="/books/">На список книг</a>')
#     else:
#         form = forms.book_id()
#
#     return render(request, template_name='blog/create_book.html',
#                   context={'form': form})


class CreateBookView(generic.CreateView):
    template_name = "blog/create_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


class SearchListView(generic.ListView):
    template_name = "blog/book_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return books.objects.filter(name__icontains=self.request.GET.get("q")).order_by(
            "-id"
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
