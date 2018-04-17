from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name= "profile", on_delete=models.CASCADE)
    gender_choices = (
        ('wanita', 'Wanita',),
        ('pria', 'Pria',),
    )
    gender = models.CharField(max_length = 10, default = "pria", choices= gender_choices)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    phone = PhoneNumberField(unique=True)
    hide_phone = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/userprofile')
    update_time = models.DateTimeField(
        default=timezone.now)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
