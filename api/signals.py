from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def assign_group_to_user(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
