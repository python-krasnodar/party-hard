"""Social auth pipelines"""
from social_core.backends.vk import VKOAuth2
from .models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    if isinstance(backend, VKOAuth2) and 'user_photo' in response:
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
        else:
            profile = Profile(user=user)

        profile.avatar_url = response.get('user_photo')
        profile.save()
