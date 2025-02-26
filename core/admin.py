from django.contrib import admin
from .models import Master, Service, Visit, Review



# Определяем классы инлайнов
class ReviewInline(admin.TabularInline):  # TabularInline отображает в виде таблицы
    model = Review
    extra = 0  # количество пустых форм для добавления
    readonly_fields = ('text', 'rating', 'created_at')
    can_delete = False  # запрет на удаление
    max_num = 10 # максимальное количество отзывов на странице
    ordering = ('-created_at',)

class VisitInline(admin.TabularInline):
    model = Visit
    extra = 0
    readonly_fields = ('created_at',)
    fields = ('name', 'phone', 'status', 'created_at')
    max_num = 10 # максимальное количество записей на странице
    ordering = ('-created_at',)

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке записей (порядок учитывается)
    list_display = ('first_name', 'last_name', 'phone')
    
    # inlines - добавляем наши инлайны
    inlines = [VisitInline, ReviewInline]
    filter_horizontal = ('services',)  # улучшенный виджет для ManyToMany поля



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Отображаемые поля в списке записей (порядок учитывается)
    list_display = ('name', 'price')
    # Поля которые будут учитываться в поиске
    search_fields = ('name', 'description')
    # Кликабельные ссылки на поля
    list_display_links = ('name', 'price')
    # Поля только на чтение
    # readonly_fields = ('description',)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Эти поля будут закрыты на редактирование для ВСЕХ!
    readonly_fields = ('text', 'rating', 'master')
    # Поля которые будут учитываться в поиске
    search_fields =  ('text', 'name', 'master')
    # Отображаемые столбцы в таблице
    list_display = ('name', 'rating', 'status', 'created_at')
    # Сортировка по created_at сверху свежие
    ordering = ('-created_at',)
    # Сколько отзывов на странице?
    list_per_page = 10
    # Фильтры. По рейтингу, мастерам, статусу и дате
    list_filter = ('rating', 'master', 'status', 'created_at')


#Visit
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    # Поля которые будут учитываться в поиске
    search_fields = ('phone', 'name', 'comment')
    # Отображаемые столбцы в таблице
    list_display = ('name', 'phone', 'created_at', 'status', 'master')
    # Сортировка по дате
    ordering = ('created_at', 'master')
    # Фильтры. По услуге, мастеру, клиенту и дате
    list_filter = ('master', 'created_at')
    filter_horizontal = ('services',)
    # filter_vertical = ('services',)

