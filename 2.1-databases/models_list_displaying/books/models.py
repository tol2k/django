# coding=utf-8
from autoslug import AutoSlugField
from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')
    slug = AutoSlugField(populate_from='pub_date')

    def __str__(self):
        return self.name + " " + self.author
