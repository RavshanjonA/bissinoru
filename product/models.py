from django.db import models


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])


class Product(models.Model):
    image = models.ImageField(upload_to=nameFile, null=False, blank=False)
    title = models.CharField(max_length=128, null=False, blank=False)
    size = models.CharField(max_length=56, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"


class Order(models.Model):
    username = models.CharField(max_length=128, null=False, blank=False)
    phone = models.CharField(max_length=56, verbose_name="Phone number", null=False, blank=False)
    products = models.ManyToManyField("product.Product", related_name="pruducts")
    address = models.TextField()
    summa = models.CharField(max_length=128, null=False, blank=False)

    @property
    def product_list(self):
        return self.products.values_list()

    def __str__(self):
        return f"{self.username} : {self.summa} "

    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Order"
        db_table = "order"
