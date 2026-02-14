# Связь 1:1
# cinema/models.py
from django.db import models

class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    # Описываем поле, ссылающееся на модель OriginalTitle:
    original_title = models.OneToOneField(
        # На какую модель ссылаемся
        OriginalTitle,
        # Поведение при удалении:
        # если оригинальное имя будет удалено,
        # то и сам фильм будет удалён.
        on_delete=models.CASCADE
    )



# Связь 1:M
# cinema/models.py
from django.db import models

class ProductType(models.Model):
    title = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE
    )



# Связь M:M
from django.db import models

class Director(models.Model):
    full_name = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    directors = models.ManyToManyField(Director)  # Вот оно, поле!



# Связь M:M ещё один вариант
from django.db import models

class Director(models.Model):
    full_name = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    # Параметр through указывает, какую модель надо назначить промежуточной:
    directors = models.ManyToManyField(Director, through='Partnership')

class Partnership(models.Model):
    # Поле, ссылающееся на модель Director:
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    # Поле, ссылающееся на модель VideoProduct:
    videoproduct = models.ForeignKey(VideoProduct, on_delete=models.CASCADE)
    # Дополнительные поля:
    # дата начала работы режиссёра над фильмом...
    date_joined = models.DateField()
    # ...и история о том, почему на фильм пригласили именно этого режиссёра.
    invite_reason = models.CharField(max_length=300)