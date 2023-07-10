from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_Client(sender, instance,created, **kwargs):
    if created:
        try:
            clientes = Group.objects.get(name='cliente')
        except Group.DoesNotExist:
            clientes = Group.objects.create(name='cliente')
        instance.user.groups.add(clientes)