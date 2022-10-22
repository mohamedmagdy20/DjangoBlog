from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
@recevier(post_save, sender=User)
def create_profile(sender,instance,created, **kwarge):
    if created:
        Profile.objects.create(user=instance)


@recevier(post_save, sender=User)
def create_profile(sender,instance, **kwarge):
    instance.profile.save()
