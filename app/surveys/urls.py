from django.conf.urls import url
from .views import SurveysListView, SurveysDetailView, SurveysCreateView, delete_survey

urlpatterns = [
    url(r'^$', SurveysListView.as_view(), name='list'),
    url(r'^create/$', SurveysCreateView.as_view(), name='create'),
    url(r'^result/(?P<pk>[0-9]+)/$', SurveysDetailView.as_view(), name='result'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete_survey, name='delete'),
]
