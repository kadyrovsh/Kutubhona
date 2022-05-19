from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Student,Muallif,Kitob, Record
admin.site.register(Record)

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ("ism", "id",)
    list_display = ("id", "ism", "yosh", "trik",)
    list_display_links = ("ism",)
    list_editable = ("yosh", "trik",)
    list_filter = ("trik",)


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ("ism", "id", "guruh",)
    list_editable = ("kitob_soni", "guruh",)
    list_filter = ("guruh",)
    list_display = ("id", "ism", "guruh", "kitob_soni",)
    list_display_links = ("ism",)

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ("nom", "id",)
    list_display = ("id", "nom", "sahifa", "janr",)
    list_display_links = ("nom",)
    list_editable = ("sahifa", "janr",)
    list_filter = ("janr",)

    autocomplete_fields = ("muallif",)

