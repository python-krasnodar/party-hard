"""
Surveys decorators module.
"""
from functools import wraps
from django.shortcuts import redirect
from config.settings import ORG_UID


def _is_org(user):
    """Check user is org"""
    user = user
    social = user.social_auth.get(provider='vk-oauth2')
    return user.is_staff or (hasattr(social, 'uid') and social.uid == ORG_UID)


def user_is_org(func):
    """Check user is organizator"""
    @wraps(func)
    def wrap(request, *args, **kwargs):
        """Before execute view, check user is organizator"""
        if _is_org(request.user):
            # is organizator
            return func(request, *args, **kwargs)
        else:
            # user from vk
            return redirect('surveys:create')

    return wrap


def user_is_not_org(func):
    """Check user is not organizator"""
    @wraps(func)
    def wrap(request, *args, **kwargs):
        """Before execute view, check user is not organizator"""
        if not _is_org(request.user):
            return func(request, *args, **kwargs)
        else:
            return redirect('surveys:list')

    return wrap
