from django.db import models

class books(models.Model):

    ganre = (
        ('Фэнтези', 'Фэнтези'),
        ('Боевик', 'Боевик'),
        ('Детектив', 'Детектив'),
        ('Драма', 'Драма'),
        ('Роман', 'Роман'),
    )

    name = models.CharField(max_length=100, verbose_name='напишите название книги')
    ganre = models.CharField(max_length=100, verbose_name='выберите жанр книги', choices=ganre)
    price = models.CharField(max_length=100, verbose_name='напишите стоимость кинги')
    image = models.ImageField(upload_to='Book/', verbose_name='загрузите фото книги')
    date_of_creation = models.DateField(verbose_name='установите дату создания книги')
    about_book = models.TextField(verbose_name='опишите книгу')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.ganre}'

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'


class ReviewBooks(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE,
                                 related_name='review_books')
    text = models.TextField()
    mark = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.book} - {self.mark}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} - {self.price}'