from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    
class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    milliseconds = models.FloatField()
    bytes = models.PositiveIntegerField()
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)

