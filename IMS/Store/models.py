# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from math import floor
from django.conf import settings
from django.contrib.auth import get_user_model 
from django.utils import timezone


class Company(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')

    def __str__(self) -> str:
        return self.c_name

    class Meta:
        managed = False
        db_table = 'company'
 
class Supplier(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.s_name

    class Meta:
        managed = False
        db_table = 'supplier'


class Product(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    quantity = models.IntegerField()
    b_cost = models.BigIntegerField()
    sell = models.IntegerField(blank=True, null=True)
    c = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    s = models.ForeignKey(Supplier, models.DO_NOTHING, blank=True, null=True)
    def __str__(self) -> str:
        return self.p_name
    def save(self, *args, **kwargs):
        if not self.sell:
            # If `sell` field is not set yet, calculate it based on `b_cost`
            self.sell = floor(self.b_cost * 0.2) + self.b_cost
        # Call the parent save method to save the instance to the database
        super().save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'product'


class MedOrder_interm(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    p = models.ForeignKey(Product,on_delete=models.CASCADE,null =True)
    update= models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(null=True)
    amount = models.IntegerField(null=True) 
    def __str__(self) -> str:
        return f'{self.p}  {self.user.username} {self.amount}'

    def save(self,*args,**kwargs):
        if self.quantity is not None and self.p is not None:
            self.amount = self.quantity *  self.p.sell
            self.p.quantity -= self.quantity
            self.p.save()
        super().save(*args,**kwargs)
# order table


