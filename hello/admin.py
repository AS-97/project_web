from django.contrib import admin
from .models import LiveText, LiveImage

@admin.register(LiveText)
class LiveTextAdmin(admin.ModelAdmin):
    list_display = ('content',)  # Zobrazí obsah textu v admin rozhraní

@admin.register(LiveImage)
class LiveImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')  # Zobrazí ID a název obrázku v přehledu admin panelu