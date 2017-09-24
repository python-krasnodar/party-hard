"""
Surveys admin module.

In this module are registered classes for the administrator ui.
"""
from django.contrib import admin
from .models import Survey


@admin.register(Survey)
class DrinkAdmin(admin.ModelAdmin):
    """Survey admin"""
    pass
