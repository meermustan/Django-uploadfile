from django.db import models
from django.utils import timezone

class Beast(models.Model):
    media = models.FileField(upload_to="media", null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)