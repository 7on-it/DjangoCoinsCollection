from django.contrib import admin
from .models import Coin

# Регистрируем модель Coin в админке
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    # Поля, которые будут видны в списке монет
    list_display = ('country', 'year', 'denomination', 'metal', 'condition', 'owner', 'added_at')
    
    # Боковая панель с фильтрацией (по стране, металлу и состоянию)
    list_filter = ('country', 'metal', 'condition', 'year')
    
    # Поле для поиска по этим полям
    search_fields = ('country', 'denomination', 'description', 'owner__username')
    
    # Сортировка по умолчанию (сначала новые)
    ordering = ('-year',)
    
    # Автоматически подставлять текущего пользователя как владельца (полезно)
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если объект новый (ещё нет id)
            obj.owner = request.user  # Назначаем владельца
        super().save_model(request, obj, form, change)