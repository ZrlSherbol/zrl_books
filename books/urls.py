from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books),
    path('book/', views.for_book_view),
    path('about me/', views.about_me),
    path('my hobby/', views.my_hobby),
    path('Time/', views.Time),
    path('random/', views.random),
    path('books/', views.books_list_view),
    path('books/<int:id>', views.books_detail_view),
]
