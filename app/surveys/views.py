"""
Surveys views module.
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from users.decorators import user_is_org, user_is_not_org
from .models import Survey
from .forms import SurveyForm
from .tasks import send_org_email


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
    form_class = SurveyForm

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Survey.objects.filter(user=user).exists():
            return redirect('surveys:result', pk=user.survey.id)
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        result = super(SurveysCreateView, self).form_valid(form)
        self._send_org_email()
        return result

    def _send_org_email(self):
        """Send email notification"""
        if self.object.going:
            # user going to party
            message = 'User {} are going to party. Selected drink: {}.'.format(
                self.object.user.get_full_name(),
                self.object.drink.title
            )
        else:
            # user not going to party
            message = 'User {} are not going to party. :('.format(
                self.object.user.get_full_name()
            )
        send_org_email.delay(message)


@login_required
@user_is_not_org
def delete_survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    user = survey.user
    survey.delete()
    message = 'User {} has deleted his survey.'.format(user.get_full_name())
    send_org_email.delay(message)
    return redirect('surveys:create')
