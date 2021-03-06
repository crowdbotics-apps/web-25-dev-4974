from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    fdsfdsfsd = models.BigIntegerField(null=True, blank=True,)
    hghghg = models.BigIntegerField(null=True, blank=True,)
    ghfhgfh = models.BigIntegerField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Shghg(models.Model):
    "Generated Model"
    hnh = models.BigIntegerField()


class GVfdfg(models.Model):
    "Generated Model"
    tryr = models.BigIntegerField()


class GFF(models.Model):
    "Generated Model"
    hgkjgh = models.BigIntegerField()
