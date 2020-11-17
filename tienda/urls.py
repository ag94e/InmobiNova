from django.contrib import admin
from django.urls import path
from gestionpedidos import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dato/', app_views.fecha_hora),
    path('edad/<int:edad>/<int:year>', app_views.calcular_edad),
    path('new/', app_views.newvista),
    path('home/', app_views.renderview),
    path('register/', app_views.register),
    path('housess/', app_views.houses_list),
    path('contact/', app_views.contact),
    path('login/', app_views.login),
    path('test/', app_views.test),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

