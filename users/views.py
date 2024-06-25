from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares


# register
class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/register.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        height = form.cleaned_data["height"]
        if height <= 140 and height >= 50:
            self.object.height = "аномальний низкий рост"
        elif height >= 140 and height >= 160:
            self.object.height = "низкий рост"
        elif height >= 160 and height <= 170:
            self.object.height = "средний рост"
        elif height >= 170 and height < 185:
            self.object.height = "высокий рост"
        elif height >= 185 and height <= 200:
            self.object.height = "очень высокий рост"
        elif height >= 200 and height <= 240:
            self.object.height = "аномально высокий рост"
        else:
            self.object.height = "рост не определен"
        self.object.save()
        return response


# authorization
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["height"] = getattr(self.request, "height", "Рост не определен")
        return context
