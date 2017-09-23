"""
Surveys models module.

In this module contains models relating to the survey data.
"""
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from dictionaries.models import Drink


class Survey(models.Model):
    """Survey model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    going = models.BooleanField(default=False)
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return string representation"""
        username = self.user.username
        is_going = _("Going") if self.going else _("Misses")
        return "{} {}".format(username, is_going)

    class Meta:
        """Model metadata"""
        ordering = ["-created_at", "-updated_at"]
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
