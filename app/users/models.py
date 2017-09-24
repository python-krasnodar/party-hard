"""
Users models module
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField()

    def __str__(self):
        """Return string representation"""
        return self.user.username
