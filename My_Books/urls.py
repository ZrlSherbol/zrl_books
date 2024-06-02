from django.urls import path
from books import views

urlpatterns = [
    path('about me/', views.about_me),
    path('my hobby/', views.my_hobby),
    path('Time/', views.Time),
    path('random/', views.random)
]
