from django.db import models
from django.db.models.functions import Now

class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_default=Now())
