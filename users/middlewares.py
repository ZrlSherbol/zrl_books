from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class HeightMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            height = int(request.POST.get("height"))
            if height <= 140 and height >= 50:
                request.height = "аномальний низкий рост"
            elif height >= 140 and height >= 160:
                request.height = "низкий рост"
            elif height >= 160 and height <= 170:
                request.height = "средний рост"
            elif height >= 170 and height < 185:
                request.height = "высокий рост"
            elif height >= 185 and height <= 200:
                request.height = "очень высокий рост"
            elif height >= 200 and height <= 240:
                request.height = "аномально высокий рост"
            else:
                return HttpResponseBadRequest("вы ввели невозможный рост")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "height", "рост не определен")
