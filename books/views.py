from django.shortcuts import render
from django.http import HttpResponse
import datetime
from random import randint

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