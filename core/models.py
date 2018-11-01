# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_random_queryset import RandomManager
from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
class proxies(models.Model):
    objects = RandomManager()
    id = models.AutoField(primary_key=True)
    sourceid = models.IntegerField(blank=False)
    proxy = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    region =models.CharField(max_length = 100)
    country =models.CharField(max_length = 100)
    countrycode =models.CharField(max_length = 10)
    booking =  models.IntegerField(blank=False)
    expedia = models.IntegerField(blank=False)
    google = models.IntegerField(blank=False)
    mmt = models.IntegerField(blank=False)
    ports = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name = "proxy"
        verbose_name_plural = "proxies"
    
