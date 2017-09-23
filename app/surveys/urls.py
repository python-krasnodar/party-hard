from django.conf.urls import url
from .views import SurveysListView, SurveysDetailView, SurveysCreateView

urlpatterns = [
    url(r'^$', SurveysListView.as_view(), name='list'),
    url(r'^create/$', SurveysCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', SurveysDetailView.as_view(), name='result'),
]
