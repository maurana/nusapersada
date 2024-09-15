import os
import re
import string
import random
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver

# storage instance
default_storage = FileSystemStorage()

def filesave(instance, filename):
    path = 'profiles/'
    profiles = str(re.sub(r"\s+", "", instance.name.lower()))
    ext = "." + filename.split('.')[-1]
    randtext = ''.join(random.choice(string.ascii_letters) for i in range(15))
    filename_reformat = profiles + '-' + randtext + ext
    return os.path.join(path, filename_reformat)

class Profiles(models.Model):
    profiles_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='PROFILES_ID')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    profiles_img = models.ImageField(upload_to=filesave,storage=default_storage)
    profiles_created_at = models.DateTimeField(auto_now_add=True)
    profiles_updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-profiles_id']

@receiver(models.signals.post_delete, sender=Profiles)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    if instance.profiles_img:
        if os.path.isfile(instance.profiles_img.path):
            os.remove(instance.profiles_img.path)

@receiver(models.signals.pre_save, sender=Profiles)
def auto_delete_file_on_change(sender, instance, *args, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Profiles.objects.get(pk=instance.pk).profiles_img
    except Profile.sDoesNotExist:
        return False

    new_file = instance.profiles_img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)