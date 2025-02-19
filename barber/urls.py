from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from core.views import VisitListView

urlpatterns = (
    [
        path("", views.IndexView.as_view(), name="index"),
        path("admin/", admin.site.urls),
        path("thanks/", views.ThanksView.as_view(), name="thanks"),
        path('visits/', VisitListView.as_view(), name='visit_list'),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)