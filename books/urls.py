from django.urls import path
from . import views

urlpatterns = [
    path('about me/', views.about_me),
    path('my hobby/', views.my_hobby),


    path('Time/', views.Time),
    path('random/', views.random),

    path('books/<int:id>/delete/', views.drop_book_view),
    path('books/<int:id>/update/', views.edit_book_view),

    path('books/', views.books_list_view),
    path('books/<int:id>', views.books_detail_view),
]
