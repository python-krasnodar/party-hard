"""
Surveys views module.
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .decorators import user_is_org, user_is_not_org
from .models import Survey


@method_decorator(login_required, name='get')
@method_decorator(user_is_org, name='get')
class SurveysListView(ListView):
    """Surveys list"""
    model = Survey


@method_decorator(login_required, name='get')
@method_decorator(user_is_not_org, name='get')
class SurveysDetailView(DetailView):
    """Surveys result view"""
    model = Survey


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_not_org, name='dispatch')
class SurveysCreateView(CreateView):
    """Surveys create view"""
    model = Survey
    fields = ['going', 'drink']

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Survey.objects.filter(user=user).exists() and hasattr(user.survey, 'id'):
            return redirect('surveys:result', pk=user.survey.id)
        else:
            return super().dispatch(request, *args, **kwargs)
