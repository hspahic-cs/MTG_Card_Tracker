from django.contrib import admin

from .models import Card

# Register your models here.
@admin.register(Card)
class cardAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'cardSet', 'cost']
