from django.shortcuts import render, redirect
from django.views.generic import View
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context




class IndexView(View):
    def get(self, request):
        context = {
            'menu': MENU,
            'masters': Master.objects.all(),
            'services': Service.objects.all(),
            'form': VisitForm()
        }
        return render(request, 'main.html', context)

    def post(self, request):
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        
        context = {
            'menu': MENU,
            'masters': Master.objects.all(),
            'services': Service.objects.all(),
            'form': form
        }
        return render(request, 'main.html', context)
