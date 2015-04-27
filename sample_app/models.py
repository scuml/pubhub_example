
from django.db import models

class Doodad(models.Model):

    """
    A generic item type.
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default='')
    status = models.TextField(blank=True, default='')
