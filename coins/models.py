from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Coin(models.Model):
    # Основные поля
    country = models.CharField('Страна', max_length=100)
    year = models.IntegerField('Год выпуска')
    denomination = models.CharField('Номинал', max_length=50)  # например, "1 рубль", "5 долларов"
    metal = models.CharField('Металл', max_length=50, blank=True)  # золото, серебро, медь...
    
    # Качество/состояние (выбор из списка)
    class Condition(models.TextChoices):
        PERFECT = 'PF', 'Превосходное (Proof)'
        UNCIRCULATED = 'UNC', 'Безупречное (UNC)'
        EXTREMELY_FINE = 'XF', 'Отличное (XF)'
        VERY_FINE = 'VF', 'Очень хорошее (VF)'
        FINE = 'F', 'Хорошее (F)'
        POOR = 'P', 'Плохое (P)'
    
    condition = models.CharField(
        'Состояние',
        max_length=3,
        choices=Condition.choices,
        default=Condition.VERY_FINE
    )
    
    # Дополнительные поля
    weight = models.FloatField('Вес (граммы)', blank=True, null=True)
    diameter = models.FloatField('Диаметр (мм)', blank=True, null=True)
    description = models.TextField('Описание', blank=True)
    
    # Фото (опционально)
    image = models.ImageField('Фото', upload_to='coins/', blank=True, null=True)
    
    # Связь с пользователем
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    added_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    
    def __str__(self):
        return f"{self.country}, {self.year} — {self.denomination}"
    
    def get_absolute_url(self):
        return reverse('coin_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
        ordering = ['-year', 'country']  # Сортировка: сначала новые, потом по стране