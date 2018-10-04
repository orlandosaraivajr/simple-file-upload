from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    image = models.ImageField(upload_to='image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
