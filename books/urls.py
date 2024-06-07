from django.urls import path
from . import views

urlpatterns = [
    path('about me/', views.about_me),
    path('my hobby/', views.my_hobby),
    path('Time/', views.Time),
    path('random/', views.random),
    path('books/', views.books_list_view),
    path('books/<int:id>', views.books_detail_view),
]
