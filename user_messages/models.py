from django.db import models
from django.conf import settings


class UserMessage(models.Model):
    recipient = models.ForeignKey(
             'user.CustomUser', on_delete=models.CASCADE,
             related_name='user_messages', default='1')
    sender = models.ForeignKey(
             settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    text = models.TextField()
