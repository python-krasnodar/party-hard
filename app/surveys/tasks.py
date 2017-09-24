"""Surveys tasks module"""
from django.core.mail import EmailMessage
from django.utils.translation import gettext as _
from celery import shared_task
from config.settings import ORG_EMAIL


@shared_task
def send_org_email(message):
    """Send email notification in background task"""
    email = EmailMessage(_('Party Hard Notification'), message, to=[ORG_EMAIL])
    email.send()
