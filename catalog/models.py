from django.db import models
from django.contrib.auth.models import *
from django.shortcuts import reverse


class Section(models.Model):
    section_name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return 'Раздел %s' % (self.section_name)

    def get_section_url(self):
        return reverse('category_list_url', kwargs={'id':self.id})

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=True)
    section = models.ForeignKey(Section, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'Категория %s' % (self.category_name)

    def get_category_url(self):
        return reverse('category_url', kwargs={'name':self.category_name})


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=50, unique=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return 'Подкатегория %s' % (self.subcategory_name)
