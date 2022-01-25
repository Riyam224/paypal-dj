from django.db import models

from django.utils.translation import gettext as _



class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    price = models.FloatField(_("price"))

    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name




class Order(models.Model):
    
    order_id = models.IntegerField(_("order id"))
    order_completed = models.BooleanField(_("order completed"))
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.order_id)
