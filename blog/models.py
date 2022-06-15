
from django.db import models
from django.db.models import Sum


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

class OrderItem(models.Model):
    # items = models.ManyToManyField("blog.Item",blank=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    sum_cost = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.sum_cost}"
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.sum_cost:
            self.sum_cost =sum(item.cost for item in self.items.all())
        super(OrderItem, self).save()

    c


