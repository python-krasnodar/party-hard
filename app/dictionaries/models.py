"""
Dictionaries models.

In this module contains models relating to the dictionaries data.
"""
from django.db import models
from django.utils.translation import ugettext as _


class Drink(models.Model):
    """Drink model"""
    title = models.CharField(max_length=255, unique=True, help_text=_("Drink title"))
    sorder = models.IntegerField(help_text=_("Sorting order in the drop-down lists"))

    def __str__(self):
        """Return string representation"""
        return self.title

    class Meta:
        """Model metadata"""
        ordering = ["sorder"]
        verbose_name = _("drink")
        verbose_name_plural = _("drinks")
