
from django.contrib import admin
from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dato/', views.fecha_hora),
    path('edad/<int:edad>/<int:year>', views.calcular_edad),
    path('new/', views.newvista),
    path('home/', views.renderview, name="home"),
    path('register/', views.register),
    path('housess/', views.houses_list),
    path('contact/', views.contact),
    path('login/', views.login),
    path('test/', views.test),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

