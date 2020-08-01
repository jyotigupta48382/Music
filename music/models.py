from django.db import models

from django.urls import reverse


# Create your models here.
class Album(models.Model):
    album_title=models.CharField(max_length=300)
    artist=models.CharField(max_length=300)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=9999999999)

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={'pk':self.pk} )

    def __str__(self):
        return self.album_title
#username:jyotigupta
#password:django123


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=300)
    song_title=models.CharField(max_length=500)
    is_fav=models.BooleanField(default=False)
    def __str__(self):
        return  self.song_title