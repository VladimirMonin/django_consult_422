import os
from celery import Celery
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barber.settings')

# Создаем экземпляр приложения Celery
app = Celery('barber')

# Загружаем конфигурацию из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
