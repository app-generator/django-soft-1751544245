# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    label = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Product(models.Model):

    #__Product_FIELDS__
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField()
    creation = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Stock(models.Model):

    #__Stock_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    lowthreshold = models.IntegerField(null=True, blank=True)

    #__Stock_FIELDS__END

    class Meta:
        verbose_name        = _("Stock")
        verbose_name_plural = _("Stock")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    creation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    type = models.CharField(max_length=255, null=True, blank=True)
    id = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Operator(models.Model):

    #__Operator_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Operator_FIELDS__END

    class Meta:
        verbose_name        = _("Operator")
        verbose_name_plural = _("Operator")


class Sale(models.Model):

    #__Sale_FIELDS__
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    creation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    paymenttype = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=255, null=True, blank=True)

    #__Sale_FIELDS__END

    class Meta:
        verbose_name        = _("Sale")
        verbose_name_plural = _("Sale")


class Itemsale(models.Model):

    #__Itemsale_FIELDS__
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    #__Itemsale_FIELDS__END

    class Meta:
        verbose_name        = _("Itemsale")
        verbose_name_plural = _("Itemsale")



#__MODELS__END
