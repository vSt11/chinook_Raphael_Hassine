from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    composer = models.CharField(max_length=100, null=True, blank=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

