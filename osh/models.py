from django.db import models


# Create your models here.
class Post(models.Model):
    """ Посты """
    title = models.CharField("Называние", max_length=50)
    img = models.ImageField("Фото", upload_to="osh/")
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Trips(models.Model):
    """ Туры """
    TOUT_TYPE = (
        ('1', 'Однодневный'),
        ('2', 'Многодневный'),
        ('3', 'Пешие')
    )

    COMPLEXITY = (
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Сложная'),
    )

    title = models.CharField("Называние", max_length=50)
    img = models.ImageField("Фото", upload_to="osh/")
    description = models.TextField("Описание")
    price = models.PositiveSmallIntegerField(default=0)
    group_size = models.PositiveSmallIntegerField('Количество чел.')
    tour_type = models.CharField('Тип тура', max_length=20, choices=TOUT_TYPE, default='1')
    complexity = models.CharField('Сложность', max_length=20, choices=COMPLEXITY, default='1')

    def __str__(self):
        return self.title

    def tour_type_v(self):
        return dict(self.TOUT_TYPE)[self.tour_type]

    def complexity_v(self):
        return dict(self.COMPLEXITY)[self.complexity]

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'


class Food(models.Model):
    """ Еда """
    title = models.CharField("Называние", max_length=50)
    img = models.ImageField("Фото")
    description = models.TextField("Описание")
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еды'
