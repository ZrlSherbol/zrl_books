from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    STUDY = (("School", "School"), ("College", "College"), ("University", "University"))

    GAME_GANRES = (
        ("Action", "Action"),
        ("Shooter", "Shooter"),
        ("Fighting", "Fighting"),
        ("Other", "Other"),
    )

    GENDER = (("Male", "Male"), ("Female", "Female"))

    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(
        default=18, validators=[MaxValueValidator(99), MinValueValidator(5)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    height = models.PositiveIntegerField(
        default=160, validators=[MaxValueValidator(250), MinValueValidator(65)]
    )
    weight = models.PositiveIntegerField(
        validators=[MaxValueValidator(300), MinValueValidator(30)]
    )
    home_address = models.CharField(max_length=30)
    hobby = models.CharField(max_length=20)
    Study = models.CharField(max_length=20, choices=STUDY)
    game_ganres = models.CharField(max_length=20, choices=GAME_GANRES)


@receiver(post_save, sender=CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно пользователь зарегистрировался")
        height = instance.height
        if height <= 140 and height >= 50:
            instance.height = "аномальний низкий рост"
        elif height >= 140 and height >= 160:
            instance.height = "низкий рост"
        elif height >= 160 and height <= 170:
            instance.height = "средний рост"
        elif height >= 170 and height < 185:
            instance.height = "высокий рост"
        elif height >= 185 and height <= 200:
            instance.height = "очень высокий рост"
        elif height >= 200 and height <= 240:
            instance.height = "aномально высокий рост"
        else:
            instance.club = "рост не определен"
        instance.save()
