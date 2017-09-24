"""
Dictionaries admin module.

In this module are registered classes for the administrator ui.
"""
from django.contrib import admin
from .models import Drink


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    """Drink admin"""
    pass
