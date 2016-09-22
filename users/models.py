from __future__ import unicode_literals
from django.contrib.auth.models import User
import os
from django.db import models
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from mainserver.settings import BASE_DIR
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.username, ext)
    return os.path.join(instance.directory_string_var, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to=content_file_name, blank=True,default="/static/dist/img/404_user.png")
    directory_string_var = 'users/picture'

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.picture:
            image = Img.open(StringIO.StringIO(self.picture.read()))
            image.thumbnail((300,400), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.picture = InMemoryUploadedFile(output,'ImageField',  self.picture.name, 'image/jpeg', output.len, None)
        super(UserProfile, self).save(*args, **kwargs)



@receiver(pre_delete, sender=UserProfile)
def userprofile_delete(sender, instance, **kwargs):
     if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


@receiver(models.signals.pre_save, sender=UserProfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = UserProfile.objects.get(pk=instance.pk).picture
    except UserProfile.DoesNotExist:
        return False

    new_file = instance.picture
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)