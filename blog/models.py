
from django.db import models

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


class Item(models.Model):
    type = models.CharField(max_length=56, null=True, blank=True)
    image = models.ImageField(upload_to=nameFile, null=False, blank=False)
    title = models.CharField(max_length=128,null=False, blank=False)
    size = models.IntegerField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    desctiption = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

