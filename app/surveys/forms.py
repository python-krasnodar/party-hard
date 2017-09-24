"""Survey forms module."""
from django import forms
from django.utils.translation import gettext as _
from .models import Survey
from dictionaries.models import Drink


class SurveyForm(forms.ModelForm):
    YESNO_CHOICES = (('', _('Please choice')), (0, _('No')), (1, _('Yes')))
    going = forms.TypedChoiceField(
        choices=YESNO_CHOICES, 
        widget=forms.Select,
        coerce=int
    )
    drink = forms.ModelChoiceField(
        queryset=Drink.objects.all(),
        widget=forms.Select,
        empty_label=_('Please choice')
    )

    class Meta:
        model = Survey
        fields = ('going', 'drink')
