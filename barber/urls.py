from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views


urlpatterns = (
    [
        path("", views.IndexView.as_view(), name="index"),
        path("admin/", admin.site.urls),
        path("thanks/", views.ThanksView.as_view(), name="thanks"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
