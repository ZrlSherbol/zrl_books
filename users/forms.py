from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (("Male", "Male"), ("Female", "Female"))

STUDY = (("School", "School"), ("College", "College"), ("University", "University"))

GAME_GANRES = (
    ("Action", "Action"),
    ("Shooter", "Shooter"),
    ("Fighting", "Fighting"),
    ("Other", "Other"),
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    home_address = forms.CharField(required=True)
    hobby = forms.CharField(required=True)
    Study = forms.ChoiceField(choices=STUDY, required=True)
    game_ganres = forms.ChoiceField(choices=GAME_GANRES, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone_number",
            "height",
            "weight",
            "home_address",
            "hobby",
            "Study",
            "game_ganres",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно пользователь зарегистрировался")
        height = instance.age
        if height <= 140 and height >= 50:
            instance.height = "аномально низкий рост"
        elif height >= 160 and height <= 170:
            instance.height = "средний рост"
        elif height >= 170 and height < 185:
            instance.height = "высокий рост"
        elif height >= 185 and height <= 200:
            instance.height = "очень высокий рост"
        elif height >= 200 and height <= 240:
            instance.height = "аномально высокий рост"
        else:
            instance.height = "вы ввели невозможный рост"
        instance.save()
