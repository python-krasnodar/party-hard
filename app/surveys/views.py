"""
Surveys views module.
"""
from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Survey


class SurveysListView(ListView):
    """Surveys list"""
    model = Survey


class SurveysDetailView(DetailView):
    """Surveys result view"""
    model = Survey


class SurveysCreateView(CreateView):
    """Surveys create view"""
    model = Survey
    fields = ['going', 'drink']
    