from autoslug import AutoSlugField
from django.db import models



class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')

