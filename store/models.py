from django.db import models
from django.contrib.auth.models import User


def upload_content_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.title.lower().replace(' ', '_'), ext)
    return filename


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default='', null=True)
    song = models.FileField(upload_to=upload_content_to)

    def __str__(self):
        return self.song.path
