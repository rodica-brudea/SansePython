from django.contrib.auth.models import User
from django.db import models


class MySongs(models.Model):
    comp_path = models.CharField(max_length=250)

    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    mel = models.ManyToManyField(User)

    class Meta:
        managed = True
        db_table = 'mysongs'

    def save(self, *args, **kwargs):
        res = str(self.comp_path)
        res2 = res.strip("\"")
        lst = res2.split("\\")
        lst = lst[:-4:-1]
        self.name = lst[0]
        self.album = lst[1]
        self.artist = lst[2]
        super().save(*args, **kwargs)            # Call the "real" save() method.

