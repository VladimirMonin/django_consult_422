# Импортируем модуль celery.py
from .celery import app as celery_app

# Делаем переменную celery_app доступной при импорте из этого пакета
__all__ = ('celery_app',)
