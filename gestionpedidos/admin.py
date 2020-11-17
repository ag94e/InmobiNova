from django.contrib import admin
from gestionpedidos.models import usuarios, houses
# Register your models here.


class usuarios_admin(admin.ModelAdmin):
    list_display = ("name", "email", "password", "city", "country")
    search_fields = ("name", "email", "city", "country")
    list_filter = ("country",)


class houses_admin(admin.ModelAdmin):
    list_display = ("city", "description", "price", "image")

admin.site.register(usuarios, usuarios_admin)
admin.site.register(houses, houses_admin)
