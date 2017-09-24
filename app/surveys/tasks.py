from celery import shared_task
from config.settings import ORG_EMAIL


@shared_task
def send_org_email(message):
    print(message)
    pass
