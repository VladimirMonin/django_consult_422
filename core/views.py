from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from .models import Master, Service, Visit
from .forms import VisitForm

MENU = [
    {'title': 'Главная', 'url': '/', 'active': True},
    {'title': 'Мастера', 'url': '#masters', 'active': True},
    {'title': 'Услуги', 'url': '#services', 'active': True},
    # {'title': 'Отзывы', 'url': '#reviews', 'active': True},
    # {'title': 'Оставить отзыв', 'url': '/review/create/', 'active': True},
    {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
]

# Импорт базовой вьюхи
from django.views.generic import View, TemplateView


# # Создание класса-наследника View
# class ThanksView(View):
#     # Переопределение метода get
#     def get(self, request):
#         # Возврат результата

#         context = {
#             'menu': MENU
#         }
#         return render(request, 'thanks.html', context)
    


class ThanksView(TemplateView):
    template_name = 'thanks.html'
    extra_context = {'menu': MENU}


class IndexView(CreateView):
    template_name = 'main.html'
    form_class = VisitForm
    success_url = 'thanks'
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        context['masters'] = Master.objects.all()
        context['services'] = Service.objects.all()
        return context