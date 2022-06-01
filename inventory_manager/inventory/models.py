from django.db import models


class Status(models.Model):
    
    class Meta:
        verbose_name_plural = 'Status'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    sku = models.CharField(max_length=254, null=True, blank=True)
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.SET_NULL)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    deletion_comment = models.CharField(max_length=254, null=True, blank=True)
