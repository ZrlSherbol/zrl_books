from django.urls import path
from . import views

urlpatterns = [
    path('about me/', views.about_me),
    path('my hobby/', views.my_hobby),
    path('Time/', views.Time),
    path('random/', views.random),

    path('BooksList/', views.BooksListView.as_view()),
    path('BooksDetail/', views.BooksDetailView.as_view()),

    path('EditBook/', views.EditBookView.as_view()),
    path('DeleteBook/', views.DeleteBookView.as_view()),
    path('CreateBooks/', views.CreateBookView.as_view()),

    path('Search/', views.SearchListView.as_view()),

]
